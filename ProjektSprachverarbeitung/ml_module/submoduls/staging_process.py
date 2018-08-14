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


def start( classifier_nn , classifier_graph ):
    liste = get_unlabeled_comments( 100 )
    print( liste )
