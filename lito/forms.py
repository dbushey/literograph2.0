from django import forms
from .models import StoryPoint



class StoryPointForm(forms.ModelForm):

    class Meta:
        model = StoryPoint
        fields = ('author', 'title', 'location_name', 'text', 'created_date',
             'latitude', 'longitude', )