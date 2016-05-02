from django.conf.urls import url
from . import views

urlpatterns = [
    # 1. Landing Page 
    url(r'^$', views.landing_page, name='landing_page'),
    
    # Writer's URLs
    # 2. Story list page
    url(r'^story/$', views.story_list, name='story_list'),
    # 3. Create new story
    url(r'^story/new/$', views.story_new, name='story_new'),
    # 4. Story detail page (create/edit/delete story points)
    url(r'^story/(?P<pk>[0-9]+)/$', views.story_detail, name='story_detail'),
    # Create new story point
    url(r'^story_point/new/(?P<pk>\d+)/$', views.story_point_new, name='story_point_new'),
    # See a single story point
    url(r'^story_point/(?P<pk>[0-9]+)/$', views.story_point_detail, name='story_point_detail'),
    # Reader's URLs
    url(r'^reader_view/(?P<pk>[0-9]+)/$', views.reader_view, name='reader_view'),
    # Cheating API for the reader view | Later add Django REST to filter story
    url(r'^story_points_json$', views.story_points_json, name='story_points_json'),
]