from django.shortcuts import render
from .models import Contacts
# Create your views here.
def Contat(request):
    Name = request.POST.get('Name',False)
    PhoneNumber = request.POST.get('PhoneNumber',False)
    Email = request.POST.get('Email',False)
    Massage = request.POST.get('Massage',False)
    cont = Contacts.objects.create(Name=Name,PhoneNumber=PhoneNumber,Email=Email,Message=Massage)
    cont.save()
    return render(request,'Contact/contact.html')