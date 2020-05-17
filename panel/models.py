from django.db import models

# Create your models here.

class RoomRate(models.Model):
    choice = [('fa' , 'Farsi'), ('eng' , 'English')]
    roomType = models.CharField(max_length=60)
    roomRate = models.DecimalField(max_digits=10, decimal_places=0)
    lang = models.CharField(choices=choice , default='fa', max_length=20)


    def __str__(self):
        return self.roomType
    

class NewsSlider(models.Model):
    title = models.CharField(max_length=60)
    body = models.CharField(max_length=250)
    image = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.title


class Weather(models.Model):
    title = models.CharField(max_length=60)
    address = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Clocklist(models.Model):
    title = models.CharField(max_length=60)
    address = models.TextField()
    
    def __str__(self):
        return self.title