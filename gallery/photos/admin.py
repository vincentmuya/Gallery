from django.contrib import admin
from .models import Editor,Image,tags

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Editor)
admin.site.register(Image,ImageAdmin)
admin.site.register(tags)
