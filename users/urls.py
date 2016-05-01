from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$', 'django.contrib.auth.views.login', name='signin'),
	url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^signup/$', views.register, name='register'),

]


