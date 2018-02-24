from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField

class tags(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length =60)
    description = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    image_image = models.ImageField(upload_to = 'images/')

    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        photos = cls.objects.filter(pub_date__date = today)
        return photos

    @classmethod
    def days_photos(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return photos

    @classmethod
    def search_by_title(cls,search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return photos
