from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from . import settings
from . import models
from .submoduls import dynamic_ml_classifier, process_comments, word_vectors, staging_process
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

print( "Read lage unlabeled comment dataframe..." )
UNLABELED_COMMENTS_DATAFRAME = pd.read_csv( settings.UNLABELED_COMMENTS_CSV_PATH )

COMMENTS_DATAFRAME = pd.read_csv( settings.COMMENTS_CSV_PATH )
#USER_LABELED_COMMENTS_DATAFRAME = pd.read_csv( settings.USER_LABELED_CSV_PATH )

COMMENTS_DATAFRAME_TEXT_ID = COMMENTS_DATAFRAME['id'].tolist()
COMMENTS_DATAFRAME_TEXT_HEADLINE = COMMENTS_DATAFRAME['headline'].tolist()
COMMENTS_DATAFRAME_TEXT_RAW = COMMENTS_DATAFRAME['text_raw'].tolist()
COMMENTS_DATAFRAME_TEXT_NORMALIZED = COMMENTS_DATAFRAME['text_normalized'].tolist()
COMMENTS_DATAFRAME_TEXT_SENTIMENT = COMMENTS_DATAFRAME['sentiment'].tolist()
COMMENTS_DATAFRAME_TEXT_SENTIMENT_NUMERICAL = COMMENTS_DATAFRAME['sentiment_numerical'].tolist()
COMMENTS_ITERATOR = 0

# running tasks
#tasks.start_staging_task( WORD2VEC_MODEL, CLASSIFIER_NN, CLASSIFIER_NN_GRAPH, schedule=10 )

# registering periodic tasks
#tasks.do_something(schedule=5)
tasks.start_staging_task( repeat=3600  )

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

    # delete entry from unlabeled comments table
    models.UserLabeledComment

    #process_comments.process_labeled_comment( comment, label_user, label_machine )
    return Response( {'Message':'Thank you for sending a labeled comment!'} )

@api_view(('GET',))
def get_unlabeled_comment_very_old( request, format='json' ):
    global COMMENTS_ITERATOR
    global CLASSIFIER
    global SENTIMENT_DICT
    comment = COMMENTS_DATAFRAME_TEXT_RAW[ COMMENTS_ITERATOR ]
    COMMENTS_ITERATOR += 1
    # 0: negative 1:neutral 2:positive
    predicted = CLASSIFIER.predict( [comment] )
    predicted_text = SENTIMENT_DICT[predicted[0]]
    print( predicted_text )
    return Response( {  'headline':COMMENTS_DATAFRAME_TEXT_HEADLINE[ COMMENTS_ITERATOR ],
                        'Message':comment,
                        'text_normalized':COMMENTS_DATAFRAME_TEXT_NORMALIZED[ COMMENTS_ITERATOR ],
                        'sentiment':COMMENTS_DATAFRAME_TEXT_SENTIMENT[ COMMENTS_ITERATOR ],
                        'sentiment_numerical':COMMENTS_DATAFRAME_TEXT_SENTIMENT_NUMERICAL[ COMMENTS_ITERATOR ],
                       'Predicted':predicted_text } )

@api_view(('GET',))
def get_unlabeled_comment_old( request, format='json' ):
    global COMMENTS_ITERATOR
    global CLASSIFIER
    global SENTIMENT_DICT
    id = COMMENTS_DATAFRAME_TEXT_ID[ COMMENTS_ITERATOR ]
    comment = COMMENTS_DATAFRAME_TEXT_RAW[ COMMENTS_ITERATOR ]
    COMMENTS_ITERATOR += 1
    # 0: negative 1:neutral 2:positive
    predicted = CLASSIFIER.predict( [comment] )
    predicted_text = SENTIMENT_DICT[predicted[0]]
    print( predicted_text )
    return Response( {  'Id':id,
                        'Message':comment,
                        'Predicted':predicted_text } )

@api_view(('GET',))
def get_unlabeled_comment( request, format='json' ):
    global COMMENTS_ITERATOR
    global CLASSIFIER
    global SENTIMENT_DICT
    global WORD2VEC_MODEL
    global CLASSIFIER_NN_GRAPH
    id = COMMENTS_DATAFRAME_TEXT_ID[ COMMENTS_ITERATOR ]
    comment = COMMENTS_DATAFRAME_TEXT_RAW[ COMMENTS_ITERATOR ]
    COMMENTS_ITERATOR += 1
    # 0: negative 1:neutral 2:positive
    staging_object = models.Staging.objects.random()
    comment = staging_object.text_raw
    comment_vector = word_vectors.comment_to_word2vec( comment, WORD2VEC_MODEL )

    with CLASSIFIER_NN_GRAPH.as_default():
        predicted = CLASSIFIER_NN.predict( [comment_vector] )

    #predicted_text = SENTIMENT_DICT[predicted[0]]
    predicted_text = str( predicted )
    print( predicted_text )
    return Response( {  'Id':id,
                        'Message':comment,
                        'Predicted':predicted_text } )

def hello_world(request):
    return render( request, 'ml_module/hello2.html', {} )

@api_view(('POST',))
def add_comment_to_db(request, format='json'):
    return Response( {'Message':'Comment added to database!'} )

@api_view(('POST',))
def dataframe_unlabeled_comments_to_database(request, format='json'):
    global UNLABELED_COMMENTS_DATAFRAME
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
