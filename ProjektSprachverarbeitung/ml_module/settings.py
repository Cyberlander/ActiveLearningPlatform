import os
ML_CLASSIFIER = "logistic_regression"
WORD_VECTORS = True

RESOURCES_BASE_PATH = "./resources"

UNLABELED_COMMENTS_CSV_PATH = os.path.join( RESOURCES_BASE_PATH, 'unlabeled_comments_raw.csv' )
COMMENTS_CSV_PATH = os.path.join( RESOURCES_BASE_PATH, 'million_post_corpus_sentiment_analysis.csv' )
USER_LABELED_CSV_PATH = os.path.join( RESOURCES_BASE_PATH, 'user_labeled_comments.csv' )

WORD2VEC_PATH = os.path.join( RESOURCES_BASE_PATH, 'word2vec/german.model' )
NN_BASE_WEIGHTS = os.path.join( RESOURCES_BASE_PATH, 'nn_clf/saved_weights.hdf5')

CLF_DICT = {
    "logistic_regression":{ "lib":"sklearn",
                            "path": os.path.join( RESOURCES_BASE_PATH, 'linear_clf/clf_sentiment_pipeline.pkl'),
                            "path_weights": ""
                            },
    "neural_network":{  "lib":"keras",
                        "path": os.path.join( RESOURCES_BASE_PATH, 'nn_clf/nn_model_word2vec.json' ) ,
                        "path_weights" : os.path.join( RESOURCES_BASE_PATH, 'nn_clf/saved_weights.hdf5' )
                     }

}
