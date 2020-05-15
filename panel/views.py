from django.shortcuts import render
from .models import RoomRate , NewsSlider

# Create your views here.

def home(request):
    roomlist = RoomRate.objects.all
    slidenews = NewsSlider.objects.all
    return render(request , 'home.html' , {'roomrate' : roomlist , 'newslider' : slidenews})
