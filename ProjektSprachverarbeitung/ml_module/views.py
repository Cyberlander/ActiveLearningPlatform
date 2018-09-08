from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from . import settings
from . import models
from .submoduls import dynamic_ml_classifier, process_comments, word_vectors, staging_process, train_neural_network
import pandas as pd
import os
import tensorflow as tf
from . import models
from . import tasks
# Create your views here.

# loading_classifier

CLF_TYPE = settings.ML_CLASSIFIER
CLASSIFIER = dynamic_ml_classifier.get_classifier( settings.ML_CLASSIFIER, **settings.CLF_DICT[settings.ML_CLASSIFIER] )

CLASSIFIER_NN = dynamic_ml_classifier.get_classifier( "neural_network", **settings.CLF_DICT[ "neural_network"] )
CLASSIFIER_NN_GRAPH = tf.get_default_graph()

WORD2VEC_MODEL = word_vectors.load_word2vec_model( settings.WORD2VEC_PATH, is_binary=True )

# running tasks
#tasks.start_staging_task( WORD2VEC_MODEL, CLASSIFIER_NN, CLASSIFIER_NN_GRAPH, schedule=10 )

# registering periodic tasks
#tasks.do_something(schedule=5)
tasks.start_staging_task( repeat=3600  )
tasks.train_neural_network_task( repeat=7200 )
#tasks.train_neural_network( schedule=5 )

SENTIMENT_DICT = {
    0:"negative",
    1:"neutral",
    2:"positive"
}


@api_view(('POST',))
def send_comment_label( request, format='json' ):
    request_data = request.data # to load body
    id = request_data['id']
    comment = request_data['comment']
    label_user = request_data['label_user']
    #row = "\n{}, {}, {}".format( comment, label_user )
    #with open( settings.USER_LABELED_CSV_PATH,"a") as target_csv_file:
        #target_csv_file.write( row )

    database_entry = models.UserLabeledComment( comment_id = id,
                                                comment = comment,
                                                label_user = label_user )
    database_entry.save()
    print( models.Staging.objects.filter( comment_id=id ))
    delete_result = models.Staging.objects.filter( comment_id=id  ).delete()
    # update unlabeled comment
    comment_from_unlabeled = models.UserLabeledComment.objects.get( comment_id=id )
    comment_from_unlabeled.is_labeled = True
    comment_from_unlabeled.save()

    #process_comments.process_labeled_comment( comment, label_user, label_machine )
    return Response( {'Message':'Thank you for sending a labeled comment!'} )


@api_view(('GET',))
def get_unlabeled_comment( request, format='json' ):
    global CLASSIFIER
    global SENTIMENT_DICT
    global WORD2VEC_MODEL
    global CLASSIFIER_NN_GRAPH
    # 0: negative 1:neutral 2:positive
    staging_object = models.Staging.objects.random()
    id = staging_object.comment_id
    comment = staging_object.text_raw
    comment_vector = word_vectors.comment_to_word2vec( comment, WORD2VEC_MODEL )

    with CLASSIFIER_NN_GRAPH.as_default():
        predicted = CLASSIFIER_NN.predict( [comment_vector] )

    predicteted_nn_negative = str(round( predicted[0][0], 3 ) )
    predicteted_nn_neutral = str(round( predicted[0][1], 3 ))
    predicteted_nn_positive = str(round( predicted[0][2], 3 ) )



    #predicted_text = SENTIMENT_DICT[predicted[0]]
    predicted_text = str( predicted )
    print( predicted_text )
    return Response( {  'Id':id,
                        'Message':comment,
                        'Predicted':predicted_text,
                        'predicteted_nn_negative':predicteted_nn_negative,
                        'predicteted_nn_neutral':predicteted_nn_neutral,
                        'predicteted_nn_positive':predicteted_nn_positive } )

def hello_world(request):
    return render( request, 'ml_module/hello2.html', {} )

@api_view(('POST',))
def add_comment_to_db(request, format='json'):
    return Response( {'Message':'Comment added to database!'} )

@api_view(('POST',))
def dataframe_unlabeled_comments_to_database(request, format='json'):
    print( "Read lage unlabeled comment dataframe..." )
    UNLABELED_COMMENTS_DATAFRAME = pd.read_csv( settings.UNLABELED_COMMENTS_CSV_PATH )
    id = UNLABELED_COMMENTS_DATAFRAME['id'].tolist()
    headline = UNLABELED_COMMENTS_DATAFRAME['headline'].tolist()
    text_raw = UNLABELED_COMMENTS_DATAFRAME['text_raw'].tolist()
    text_normalized = UNLABELED_COMMENTS_DATAFRAME['text_normalized'].tolist()
    print( "Insert dataframe entries into database" )

    rows_2_insert = len(id)
    rows_2_insert = 100000
    # just the first 100 000 for the beginning

    for i in range(rows_2_insert):
        new_entry = models.UnlabeledComment.objects.create( comment_id=id[i],
                                                    title=headline[i],
                                                    text_raw=text_raw[i] )
        print( "Row {} inserted".format( i ) )
    return Response( {'Message':'Dataframe added to database!'} )

@api_view(('POST',))
def trigger_staging_event(request, format='json'):
    global WORD2VEC_MODEL
    global CLASSIFIER_NN
    global CLASSIFIER_NN_GRAPH
    if staging_process.is_staging_area_empty():
        staging_process.start( WORD2VEC_MODEL, CLASSIFIER_NN, CLASSIFIER_NN_GRAPH )
        return Response( { 'Message':'Staging event triggered!' } )
    else:
        return Response( { 'Message':'Staging area not empty!' } )

@api_view(('POST',))
def get_labeled_comments_table_as_json(request, format='json'):
    answer = { "comments" : [] }
    all_labeled_comments = list( models.UserLabeledComment.objects.all() )
    comment_ids = []
    comments = []
    comment_labels = []
    for c in all_labeled_comments:
        json_object = { "comment_id" : c.comment_id,
                        "comment" : c.comment,
                        "label_user" : c.label_user,
                        "label_user_alphanumerical" : SENTIMENT_DICT[int( c.label_user )] }
        answer["comments"].append( json_object )
    return Response( answer )

@api_view(('GET',))
def get_database_statistics(request, format='json'):
    count_unlabeled_comments = models.UnlabeledComment.objects.filter( is_labeled=False ).count()
    l = models.UnlabeledComment.objects.filter( is_labeled=True ).count()
    print("L:", l)
    count_labeled_comments = models.UserLabeledComment.objects.count()
    count_staging_area = models.Staging.objects.count()

    return Response( { "count_unlabeled_comments" : count_unlabeled_comments,
                        "count_labeled_comments" : count_labeled_comments,
                        'count_staging_area' : count_staging_area } )
