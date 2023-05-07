from django.db import models

# Create your models here.
class Blogs(models.Model):
    Image = models.CharField(max_length=100,name="Image")
    Title = models.CharField(max_length=50,name="Title")
    Description = models.TextField(max_length=500,name="Description",default="")

    def GetImage(self):
        return '/images/' + self.Image