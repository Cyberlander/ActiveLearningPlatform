import os
ML_CLASSIFIER = "logistic_regression"

RESOURCES_BASE_PATH = "C:/Users/Felix/Documents/Coding-Projekte/Sprachverarbeitung/ProjektSprachverarbeitung/resources"

COMMENTS_CSV_PATH = os.path.join( RESOURCES_BASE_PATH, 'million_post_corpus_sentiment_analysis.csv' )
USER_LABELED_CSV_PATH = os.path.join( RESOURCES_BASE_PATH, 'user_labeled_comments.csv' )

CLF_DICT = {
    "logistic_regression":{ "lib":"sklearn",
                            "path": os.path.join( RESOURCES_BASE_PATH, 'linear_clf/clf_sentiment_pipeline.pkl')}

}
