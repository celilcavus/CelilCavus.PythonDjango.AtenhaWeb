from django.db import models

# Create your models here.
class Abouts(models.Model):
    Image = models.CharField(max_length=100,name="Image")
    Title = models.CharField(max_length=100,name="Title")
    Description = models.TextField(max_length=500,default="",name="Description")

    def GetImage(self):
        return '/Images/' + self.Image