from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

class Category(models.Model):
    category = models.CharField(max_length = 30)

    def __str__(self):
        return self.category


    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

class Image(models.Model):
    title = models.CharField(max_length =60)
    description = models.TextField()
    editor = models.ForeignKey(Editor)
    category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    image_image = models.ImageField(upload_to = 'images/', blank = True, null = True)

    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        photos = cls.objects.filter(pub_date__date = today)
        return photos

    @classmethod
    def days_photos(cls,date):
        photos = cls.objects.filter(pub_date__date = date)
        return photos

    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return photos
