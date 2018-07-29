from sklearn.externals import joblib

CLASSIFIER_DICT = {
    "logistic_regression":""
}

def load_sklearn_classifier( path ):
    clf = joblib.load( path )
    return clf


def get_classifier( clf_name, lib="sklearn", path="" ):
    if clf_name == "logistic_regression":
        clf = load_sklearn_classifier( path )
    return clf
