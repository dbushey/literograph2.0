from django.shortcuts import render, get_object_or_404
from django.utils import timezone

def user(request):
    user = User.objects.all()
    return render(request, 'users/signin.html', {'user': user})
