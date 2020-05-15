from django.contrib import admin
from .models import RoomRate , NewsSlider

# Register your models here.

@admin.register(RoomRate)

class showmodels(admin.ModelAdmin):
    list_display = ('roomType', 'roomRate')
    search_fields = ('roomType',)
    
@admin.register(NewsSlider)

class News(admin.ModelAdmin):
    list_display = ('title',)