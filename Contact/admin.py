from django.contrib import admin
from .models import Contacts
# Register your models here.
class Contact(admin.ModelAdmin):
    list_display = ("id",'Name','Message')



admin.site.register(Contacts,Contact)