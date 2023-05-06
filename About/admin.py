from django.contrib import admin
from . import models
# Register your models here.
class About(admin.ModelAdmin):
    list_display = ('id','Title')


admin.site.register(models.Abouts,About)