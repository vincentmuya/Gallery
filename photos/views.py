from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Image

# Create your views here.
def photos_today(request):
    date = dt.date.today()
    photos = Image.todays_photos()
    return render(request, 'all-photos/today-photos.html', {"date": date,"photos":photos})

def past_days_photos(request,past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_today)

    photos = Article.days_photos(date)
    return render(request, 'all-photos/past-photos.html', {"date": date})


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_categoty(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})