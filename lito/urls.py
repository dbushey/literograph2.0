from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.reader_view, name='reader_view'),
    url(r'^story_points_json$', views.story_points_json, name='story_points_json'),
    
]