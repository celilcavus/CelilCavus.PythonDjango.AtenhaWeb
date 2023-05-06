from django.contrib import admin
from . import models
# Register your models here.
class Blog(admin.ModelAdmin):
    list_display = ("id",'Title')


admin.site.register(models.Blogs,Blog)