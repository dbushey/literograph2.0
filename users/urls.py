from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout'),
]