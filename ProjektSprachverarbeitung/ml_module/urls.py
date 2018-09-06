from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url( r'^$', views.hello_world, name='hello_world' ),
    url( r'^send_comment_label',views.send_comment_label, name='send_comment_label'),
    url( r'^get_unlabeled_comment',views.get_unlabeled_comment, name='get_unlabeled_comment'),
    url( r'^dataframe_unlabeled_comments_to_database',views.dataframe_unlabeled_comments_to_database, name='dataframe_unlabeled_comments_to_database'),
    url( r'^trigger_staging_event',views.trigger_staging_event, name='trigger_staging_event'),
    url(r'^', views.get_labeled_comments_table_as_json, name='get_labeled_comments_table_as_json' )
]
