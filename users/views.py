from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in automatically in next two lines
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            # TODO Redirect should be updated to request the '?next='' paramter
            return HttpResponseRedirect("/story/")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {
        'form': form,
    })

def user(request):
    user = User.objects.all()
    return render(request, 'users/signin.html', {'user': user})
