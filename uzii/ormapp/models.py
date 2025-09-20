from django.db import models
from django.contrib import admin
class Car(models.Model):
    carnumber=models.IntegerField()
    mname=models.CharField(max_length=100)
    colour=models.IntegerField()
    year=models.IntegerField()
    price=models.FloatField()

class CarAdmin(admin.ModelAdmin):
    list_display=('carnumber','mname','colour','year','price')