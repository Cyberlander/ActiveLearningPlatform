from keras.preprocessing.text import text_to_word_sequence
sklearn_classifier = [ 'logistic_regression' ]



def textual_label_to_numeric():
    return None

def label_comment_sklearn( clf, comment ):
    predicted = clf.predict( [comment] )
    print("Predicted: ", predicted)


def process_labeled_comment( comment, label_user, label_machine ):
    print( comment, label_user, label_machine )
    print( "Comment: ", comment )
    print( "Label user:", label_user )
    print( "Label machine: ", label_machine )
    #if clf_type in sklearn_classifier:
        #label_comment_sklearn( clf, comment )
