from django.db import models

# Create your models here.
class Service(models.Model):
    Image = models.CharField(max_length=50,name="Image")
    Title = models.CharField(max_length=50,name="Title")
    Description = models.CharField(max_length=50,name="Description")

    def getImage(self):
        return '/images/' + self.Image
