from django.shortcuts import render
from .models import Blogs
# Create your views here.

def Blog(request):
    model = Blogs.objects.all()
    context = {
        'blog':model
    }
    return render(request,'blog/blog.html',context)