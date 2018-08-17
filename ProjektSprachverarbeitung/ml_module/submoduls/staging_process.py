import numpy as np
from keras.preprocessing.text import text_to_word_sequence
from . import word_vectors
from .. import models

def is_staging_area_empty():
    num_rows = len(list(models.Staging.objects.all()))
    if num_rows > 0:
        return False
    else:
        return True

def get_unlabeled_comments( number ):
    liste = []
    for i in range( number ):
        random_entry = models.UnlabeledComment.objects.random()
        liste.append( random_entry )
    return liste

def get_sentences_as_vectors( sentences_tupel, word2vec_model ):
    sentences_as_vectors_tupel = []
    for entry in sentences_tupel:
        new_entry = ( entry[0], entry[1], word_vectors.comment_to_word2vec( entry[1], word2vec_model ) )
        sentences_as_vectors_tupel.append( new_entry )
    return sentences_as_vectors_tupel

def make_nn_predictions( sentences_as_vectors_tupel, classifier_nn, classifier_graph ):
    sentences_with_predictions=[]
    for entry in sentences_as_vectors_tupel:
        with classifier_graph.as_default():
            predicted = classifier_nn.predict( entry[2] )
        sentences_with_predictions.append( (entry[0], entry[1],entry[2], predicted ) )
    return sentences_with_predictions

# highest value selection
def is_value_below_threshold( probabilities, threshold ):
    max_element = np.amax( probabilities )
    if max_element < threshold:
        return True
    else:
        return False


def do_compare_selection( tripel ):
    print()

def do_selection( sentences_with_predictions ):
    sparse_list = []
    for entry in sentences_with_predictions:
        probabilities = entry[3]
        if is_value_below_threshold( probabilities, 0.57 ):
            sparse_list.append( entry  )
    return sparse_list

def write_to_staging( sparse_list ):
    for entry in sparse_list:
        staging_entry = models.Staging.objects.create( comment_id=entry[0], text_raw=entry[1])
    print( "Wrote {} items to staging area".format( len(sparse_list ) ) )

def start( word2vec_model, classifier_nn , classifier_graph ):
    liste_model_unlabeled_comments = get_unlabeled_comments( 100 )
    predictions = []
    sentences_tupel = []
    #print(type(liste_model_unlabeled_comments))
    for i,entry in enumerate( liste_model_unlabeled_comments ):
        sentences_tupel.append( ( entry.comment_id, entry.text_raw) )
    sentences_as_vectors_tupel = get_sentences_as_vectors( sentences_tupel, word2vec_model )
    sentences_with_predictions = make_nn_predictions( sentences_as_vectors_tupel, classifier_nn, classifier_graph )
    sparse_list = do_selection( sentences_with_predictions )
    write_to_staging( sparse_list )
