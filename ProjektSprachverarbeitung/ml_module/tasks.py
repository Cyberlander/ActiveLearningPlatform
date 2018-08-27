from background_task import background
import tensorflow as tf
from . import settings
from .submoduls import dynamic_ml_classifier, word_vectors, staging_process

@background(schedule=10)
def do_something():
    print("Do something")

@background(schedule=10)
def start_staging_task():
    word2vec_model = word_vectors.load_word2vec_model( settings.WORD2VEC_PATH, is_binary=True )
    classifier_nn = dynamic_ml_classifier.get_classifier( "neural_network", **settings.CLF_DICT[ "neural_network"] )
    classifier_nn_graph = tf.get_default_graph()
    print("Executing task for staging event...")
    if staging_process.is_staging_area_empty():
        print("Staging area empty. Begin with task")
        staging_process.start( word2vec_model, classifier_nn, classifier_nn_graph )
    else:
        print( "The staging area is not empty. Task canceled." )
