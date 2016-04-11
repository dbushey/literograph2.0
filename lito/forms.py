from django import forms
from .models import StoryPoint



class StoryPointForm(forms.ModelForm):

    class Meta:
        model = StoryPoint
        fields = ('title', 'location_name', 'latitude', 'longitude',)