from django import forms
from .models import StoryPoint, Story
from django.forms import Textarea


class StoryPointForm(forms.ModelForm):

    class Meta:
        model = StoryPoint
        fields = ('title', 'location_name', 'latitude', 'longitude', 'text',
                  'img_url','soundcloud_url', 'youtube_url',)
        

class StoryForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ('title', 'description',)
        widgets = {
            'description': Textarea(attrs={'cols': 50, 'rows': 5}),
        }