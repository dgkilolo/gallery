from django.shortcuts import render, redirect, Http404
import datetime as datetime
from .models import Image


# Create your views here.
def gallery(request):
  return render(request,'gallery.html')
