from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import *

class Signup(generic.CreateView):
   form_class = UserCreationForm
   success_url =reverse_lazy('home')
   template_name='signup.html'


class Projectpage(TemplateView):
    template_name = 'pro.html'

class Videopage(ListView):
    template_name = 'video.html'
    model = Music

class Kenyanpage(ListView):
    model = Music
    template_name = 'kenyan.html'










# Create your views here.
