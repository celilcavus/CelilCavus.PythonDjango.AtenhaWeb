from django.contrib import admin
from . import models
# Register your models here.
class Service(admin.ModelAdmin):
    list_display = ('id','Title')


admin.site.register(models.Service,Service)
