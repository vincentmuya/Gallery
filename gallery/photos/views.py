from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404

# Create your views here.
def photos_today(request):
    date = dt.date.today()
    return render(request, 'all-photos/today-photos.html', {"date": date,})

def photos_of_day(request):
    date = dt.date.today()
    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
        <html>
        <body>
            <h1> {date.day}-{date.month}-{date.year}</h1>
        </body>
        </html>
            '''
    return HttpResponse(html)

def past_days_photos(request,past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)


    return render(request, 'all-photos/past-photos.html', {"date": date})
