from django.shortcuts import render, redirect, Http404
import datetime as datetime
from .models import Image


# Create your views here.
# def gallery(request):
#   return render(request,'gallery.html')

def gallery(request):
  images = Image.all_images()
  return render(request, 'gallery.html', {'images':images} )
