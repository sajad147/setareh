from django.shortcuts import render
from .models import RoomRate , NewsSlider , Weather , Clocklist

# Create your views here.

def home(request):
    roomlisten = RoomRate.objects.filter(lang='eng')
    roomlistfa = RoomRate.objects.filter(lang='fa')
    slidenews = NewsSlider.objects.all()
    weather = Weather.objects.filter(active= True)
    clock = Clocklist.objects.filter()
    return render(request , 'home.html' , {'roomrateen' : roomlisten , 'roomratefa' : roomlistfa ,'newslider' : slidenews , 'activeslider': slidenews.first() ,'weather':weather , 'clock' : clock[:4]})
