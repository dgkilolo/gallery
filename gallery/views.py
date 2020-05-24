from django.shortcuts import render, redirect, Http404
import datetime as datetime
from .models import Image


# Create your views here.
# def gallery(request):
#   return render(request,'gallery.html')

def gallery(request):
  images = Image.all_images()
  return render(request, 'gallery.html', {'images':images} )

def search_results(request):
  if 'article' in request.GET and request.GET["article"]:
    search_term = request.GET.get("article")
    search_category = Image.search_by_category(search_term)
    message = f"{search_term}"

    return render(request, 'search.html', {"message":message, "articles":search_category})

  else:
    message = "You haven't searched for any term"
    return render(request, 'search.html', {"message":message} )
