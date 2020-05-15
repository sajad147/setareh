from django.db import models

# Create your models here.

class RoomRate(models.Model):
    roomType = models.CharField(max_length=60)
    roomRate = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.roomType
    

class NewsSlider(models.Model):
    title = models.CharField(max_length=60)
    body = models.CharField(max_length=250)
    image = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.title