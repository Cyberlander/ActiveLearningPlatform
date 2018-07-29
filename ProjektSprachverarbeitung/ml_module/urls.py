from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url( r'^$', views.hello_world, name='hello_world' ),
    url( r'^send_comment_label',views.send_comment_label, name='send_comment_label'),
    url( r'^get_unlabeled_comment',views.get_unlabeled_comment, name='get_unlabeled_comment'),
]
