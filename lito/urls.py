from django.conf.urls import url
from . import views

urlpatterns = [
    # 1. Landing Page 
    url(r'^$', views.landing_page, name='landing_page'),
    # Cheating API for the reader view | Later add Django REST to filter story
    url(r'^story_points_json$', views.story_points_json, name='story_points_json'),
    # 2. Writer's page
    #url(r'^writer/story/$', views.writer_story_list, name='writer_story_list'),
    # 3. Writer create new story
    #url(r'^writer/story/new/$', views.writer_story_new, name='writer_story_new'),
    # 4. Writer story detail page (create/edit/delete story points)
    #url(r'^writer/story/(?P<pk>[0-9]+)/$', views.writer_story_detail, name='writer_story_detail'),
    # Create new story point
    url(r'^story_point/new/$', views.story_point_new, name='story_point_new'),
    # See a single story point
    url(r'^story_point/(?P<pk>[0-9]+)/$', views.story_point_detail, name='story_point_detail'),
    # Go to a particular story
    url(r'^story/(?P<pk>[0-9]+)/$', views.story_detail, name='story_detail'),
    url(r'^reader_view/$', views.reader_view, name='reader_view'),

]