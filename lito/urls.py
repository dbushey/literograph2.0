from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.reader_view, name='reader_view'),
    url(r'^story_points_json$', views.story_points_json, name='story_points_json'),
    # Create new story point
    url(r'^story_point/new/$', views.story_point_new, name='story_point_new'),
    # See a single story point
    url(r'^story_point/(?P<pk>[0-9]+)/$', views.story_point_detail, name='story_point_detail'),
]