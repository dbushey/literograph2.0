from django.contrib import admin
from .models import Story
from .models import StoryPoint
from .models import Location


admin.site.register(Story)
admin.site.register(StoryPoint)
admin.site.register(Location)