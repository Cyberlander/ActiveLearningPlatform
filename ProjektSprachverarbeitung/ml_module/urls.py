from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url( r'^$', views.hello_world, name='hello_world' ),
    url( r'^send_comment_label',views.send_comment_label, name='send_comment_label'),
    url( r'^get_unlabeled_comment',views.get_unlabeled_comment, name='get_unlabeled_comment'),
    url( r'^dataframe_unlabeled_comments_to_database',views.dataframe_unlabeled_comments_to_database, name='dataframe_unlabeled_comments_to_database'),
    url( r'^trigger_staging_event',views.trigger_staging_event, name='trigger_staging_event'),
    url(r'^get_labeled_comments_table_as_json', views.get_labeled_comments_table_as_json, name='get_labeled_comments_table_as_json' ),
    url(r'^get_database_statistics', views.get_database_statistics, name='get_database_statistics' ),
    url(r'^new_endpoint', views.new_endpoint, name='new_endpoint' ),
    url(r'^train_neural_network', views.train_neural_network, name='train_neural_network' ),
    url(r'^get_neural_network_table_as_json', views.get_neural_network_table_as_json, name='get_neural_network_table_as_json' ),
    url(r'^get_neural_network_weights_as_hdf5', views.get_neural_network_weights_as_hdf5, name='get_neural_network_weights_as_hdf5' ),
]
