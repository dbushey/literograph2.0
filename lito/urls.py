from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.reader_view, name='reader_view'),
    
]