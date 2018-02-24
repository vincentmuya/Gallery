from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.photos_today,name = 'photosToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photos,name = 'pastPhotos')
]
