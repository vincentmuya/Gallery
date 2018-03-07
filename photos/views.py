from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http  import HttpResponse,Http404
from .models import Image

# Create your views here.
def photos_today(request):
    photos = Image.todays_photos()
    return render(request, 'all-photos/today-photos.html', {"photos":photos})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_categoty(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})
