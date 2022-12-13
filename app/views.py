from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    LWO=webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpage.html',d)

def display_Accessrecords(request):
    LAO=Access_records.objects.all()
    d={'LAO':LAO}
    return render(request,'display_Accessrecords.html',d)