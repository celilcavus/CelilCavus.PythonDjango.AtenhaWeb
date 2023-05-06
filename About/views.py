from django.shortcuts import render
from .models import Abouts

# Create your views here.
def Index(request):
    model =  Abouts.objects.last()
    context = {
        'about': model
    }
    return render(request,'About/Index.html',context)