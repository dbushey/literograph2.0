from django.db import models
from django.utils import timezone

class Story (models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class StoryPoint (models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitute = models.DecimalField(max_digits=9, decimal_places=6, null=True) 
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Location (models.Model):
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitute = models.DecimalField(max_digits=9, decimal_places=6) 
	location_name = models.CharField(max_length=200)