from django.db import models
from django.utils.html import mark_safe
# Create your models here.
 
class Category(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    description = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.name

  
class Photo(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    image = models.ImageField(null=False,blank=False,upload_to = "media")

    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
        return ""


class AboutTitle(models.Model):
    title = models.CharField(max_length=100,null=False, blank=False)

    def __str__(self):
        return self.title
