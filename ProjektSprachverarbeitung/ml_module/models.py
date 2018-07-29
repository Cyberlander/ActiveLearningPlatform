from django.db import models

class UnlabeledComment(models.Model):
    title = models.CharField(max_length=255)
    text_raw = models.TextField()
    def __str__(self):
        current_comment = self.comment
        if len(current_comment)>20:
            return current_comment[:20]
        else:
            return current_comment

class UserLabeledComment( models.Model ):
    comment_id = models.CharField( max_length=255 )
    comment = models.TextField()
    label_user = models.CharField( max_length=255 )
    label_machine = models.CharField( max_length=255 )
    def __str__(self):
        current_comment = self.comment
        if len(current_comment)>20:
            return current_comment[:20]
        else:
            return current_comment
