from django.shortcuts import render
from .models import StoryPoint
import json
from django.http import HttpResponse
from django.core import serializers

def reader_view(request):
    return render(request, 'lito/reader_view.html', {'reader_view': reader_view})

def story_points_json(request):
    storypoints_as_json = serializers.serialize('json', StoryPoint.objects.all())
    return HttpResponse(json.dumps(storypoints_as_json), content_type='application/json') 