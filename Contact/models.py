from django.db import models

# Create your models here.
class Contacts(models.Model):
    Name = models.CharField(max_length=50,name="Name")
    PhoneNumber = models.CharField(max_length=20,name="PhoneNumber")
    Email = models.CharField(max_length=50,name="Email")
    Message = models.TextField(max_length=500,default="",name="Message")