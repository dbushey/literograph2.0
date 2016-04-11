from django.shortcuts import render, get_object_or_404
from .models import StoryPoint
import json
from django.http import HttpResponse
from django.core import serializers
from .forms import StoryPointForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def reader_view(request):
    return render(request, 'lito/reader_view.html', {'reader_view': reader_view})

def story_points_json(request):
    storypoints_as_json = serializers.serialize('json', StoryPoint.objects.all())
    return HttpResponse(json.dumps(storypoints_as_json), content_type='application/json') 

def story_point_detail(request, pk):
    story_point = get_object_or_404(StoryPoint, pk=pk)
    return render(request, 'lito/story_point_detail.html', {'story_point': story_point})

def story_point_new(request):
    add_story_point = StoryPointForm()
    return render(request, 'lito/story_point_edit.html', {'form': form})

@login_required
def story_point_new(request):
    if request.method == "POST":
        form = StoryPointForm(request.POST)
        if form.is_valid():
            story_point = form.save(commit=False)
            story_point.author = request.user
            story_point.save()
            return redirect('story_point_detail', pk=story_point.pk)
    else:
        form = StoryPointForm()
    return render(request, 'lito/story_point_edit.html', {'form': form})