from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse

from basic_app.forms import SignUpForm
# Create your views here.

def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    registered = False

    if request.method == "POST":
        user_form = SignUpForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password = user.password
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = SignUpForm()

    return render(request, 'basic_app/register.html',
                  {'user_form': user_form,
                   'registered': registered})

