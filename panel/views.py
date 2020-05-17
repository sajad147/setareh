from django.shortcuts import render
from .models import RoomRate , NewsSlider , Weather , Clocklist

# Create your views here.

def home(request):
    roomlist = RoomRate.objects.filter(lang='eng')
    slidenews = NewsSlider.objects.all
    weather = Weather.objects.filter(active= True)
    clock = Clocklist.objects.filter()
    return render(request , 'home.html' , {'roomrate' : roomlist , 'newslider' : slidenews , 'weather':weather , 'clock' : clock[:4]})
