from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/books/")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {
        'form': form,
    })

def user(request):
    user = User.objects.all()
    return render(request, 'users/signin.html', {'user': user})
