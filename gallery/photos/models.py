from django.db import models

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