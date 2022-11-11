from cgitb import html
from django.shortcuts import render
from django.utils import timezone
from .models import correspondecia
# Create your views here.

def index(Request):
    posts = correspondecia.objects.filter(fecha_recepcion__lte=timezone.now()).order_by('fecha_recepcion')
    return render(Request, "core/index.html", {'posts': posts})

def home(Request):
    posts = correspondecia.objects
    return render(Request, "core/index.html", {'posts': posts})





