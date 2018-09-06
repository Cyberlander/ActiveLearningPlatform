from django.db import models
from django.db.models.aggregates import Count
from random import randint
from django.db.models import Q

class UnlabeledCommentManager(models.Manager):
    def random(self):
        count = self.aggregate( count=Count('id', filter=Q(unlabeledcomment=False)))['count']
        random_index = randint(0, count-1)
        return self.filter(is_labeled=False)[random_index]

class UnlabeledComment(models.Model):
    objects = UnlabeledCommentManager()
    comment_id = models.IntegerField( unique=True )
    title = models.CharField(max_length=255)
    text_raw = models.TextField()
    is_labeled = models.BooleanField(default=False)
    def __str__(self):
        current_comment = self.text_raw
        if len(current_comment)>20:
            return current_comment[:20]
        else:
            return current_comment

class StagingManager(models.Manager):
    def random(self):
        count = self.aggregate( count=Count('id', filter=Q(staging__is_labeled=False)))['count']
        random_index = randint(0, count-1)
        return self.filter(is_labeled=False)[random_index]

class Staging(models.Model):
    objects = StagingManager()
    comment_id = models.IntegerField( unique=True )
    text_raw = models.TextField()
    is_labeled = models.BooleanField(default=False)
    def __str__(self):
        current_comment = self.text_raw
        if len(current_comment)>20:
            return current_comment[:20]
        else:
            return current_comment

class UserLabeledComment( models.Model ):
    comment_id = models.CharField( max_length=255 )
    comment = models.TextField()
    label_user = models.CharField( max_length=255 )
    def __str__(self):
        current_comment = self.comment
        if len(current_comment)>20:
            return current_comment[:20]
        else:
            return current_comment
