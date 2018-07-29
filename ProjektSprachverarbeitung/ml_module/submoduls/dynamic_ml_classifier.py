from sklearn.externals import joblib
from keras.models import model_from_json


def load_sklearn_classifier( path ):
    clf = joblib.load( path )
    return clf

def load_keras_nn_classifier( path, path_weights ):
    with open( path, "r" ) as fi:
        json = fi.read()
    model = model_from_json( json )
    model.load_weights( path_weights )
    model.summary()
    return model



def get_classifier( clf_name, lib="sklearn", path="", path_weights="" ):
    if clf_name == "logistic_regression":
        clf = load_sklearn_classifier( path )
    elif clf_name == "neural_network":
        clf = load_keras_nn_classifier( path, path_weights )
    return clf
