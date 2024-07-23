from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return render(request,"About.html") 