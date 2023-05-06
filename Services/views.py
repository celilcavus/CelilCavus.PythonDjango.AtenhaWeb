from django.shortcuts import render
from .models import Service
# Create your views here.
def Services(request):
    model = Service.objects.all()
    context = {
        'services':model
   }
    return render(request,'services/service.html',context)