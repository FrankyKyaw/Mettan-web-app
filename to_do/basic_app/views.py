from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

from basic_app.forms import SignUpForm
from . import models

# Create your views here.

def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

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

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            return HttpResponse("Invalid login details")
    else:
        return render(request,'basic_app/login.html',{})

class TaskList(ListView):
    model = models.Task

class TaskDetail(DetailView):
   model = models.Task

class TaskCreate(CreateView):
    model = models.Task
    fields = '__all__'
    success_url = reverse_lazy('basic_app:task_list')

class TaskUpdate(UpdateView):
    fields = '__all__'
    model = models.Task
    success_url = reverse_lazy('basic_app:task_list')


