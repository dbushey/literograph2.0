from django.shortcuts import render, get_object_or_404
from .models import StoryPoint, Story, Location
import json
from django.http import HttpResponse
from django.core import serializers
from .forms import StoryPointForm, StoryForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def landing_page(request):
    story_list = Story.objects.all()
    return render(request, 'lito/landing_page.html', {'story_list': story_list})

@login_required
def story_list(request): 
    author = request.user
    story_list = Story.objects.filter(author=author)
    return render(request, 'lito/story_list.html', {'story_list': story_list})

@login_required
def story_new(request):
    form = StoryForm()
    return render(request, 'lito/story_edit.html', {'form': form})

@login_required
def story_new(request):
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.save()
            return redirect('story_detail', pk=story.pk)
    else:
        form = StoryForm()
    return render(request, 'lito/story_edit.html', {'form': form})

@login_required
def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    story_points_list = StoryPoint.objects.filter(story=story)
    return render(request, 'lito/story_detail.html', {'story': story, 'story_points_list': story_points_list})

def story_point_detail(request, pk):
    story_point = get_object_or_404(StoryPoint, pk=pk)
    return render(request, 'lito/story_point_detail.html', {'story_point': story_point})

def story_point_new(request):
    add_story_point = StoryPointForm()
    return render(request, 'lito/story_point_edit.html', {'form': form})

@login_required
def story_point_new(request, pk):
    if request.method == "POST":
        form = StoryPointForm(request.POST)
        story = get_object_or_404(Story, pk=pk)
        if form.is_valid():
            story_point = form.save(commit=False)
            story_point.author = request.user
            story_point.story = story
            if story_point.youtube_url:
                story_point.youtube_url = parse_yt_url(story_point.youtube_url)
            story_point.num_order = set_num_order(story)
            story_point.save()
            return redirect('story_point_detail', pk=story_point.pk)
    else:
        form = StoryPointForm()
    return render(request, 'lito/story_point_edit.html', {'form': form})

def reader_view(request, pk):
    story = get_object_or_404(Story, pk=pk)
    story_points_list = StoryPoint.objects.filter(story=story)
    return render(request, 'lito/reader_view.html', {'story': story, 'story_points_list': story_points_list})

def story_points_json(request, pk):
    story = get_object_or_404(Story, pk=pk) 
    storypoints_as_json = serializers.serialize('json', StoryPoint.objects.filter(story=story))
    return HttpResponse(json.dumps(storypoints_as_json), content_type='application/json') 

def parse_yt_url(url):
    embed_url = "https://www.youtube.com/embed/{}"
    return embed_url.format(url.split("=")[1])

def set_num_order(story):
    story_points_list = StoryPoint.objects.filter(story=story)
    print(story_points_list)
    try:
        largest = max(story_point.num_order for story_point in story_points_list)
    except ValueError: 
        return 1
        
    return largest + 1







