from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return render(request,"About.html")

def aboutIndex(request):
    return render(request,"Index.html") 

def aboutContact(request):
    return render(request,"Contact.html")

def aboutMenu(request):
    return render(request,"Menu.html")