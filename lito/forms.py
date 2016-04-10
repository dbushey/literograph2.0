from django import forms
from .models import StoryPoint



class StoryPointForm(forms.ModelForm):

    class Meta:
        model = StoryPoint
        fields = ( 'author', 'title', 'text', 'location_name', 'latitude', 'longitude',)