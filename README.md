# Ex02 Django ORM Web Application
## Date: 20/09/2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
~~~
admin.py
from django.contrib import admin
from .models import Car,CarAdmin
admin.site.register(Car,CarAdmin)

models.py
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

~~~    




## OUTPUT
![alt text]({CF4463D9-4B49-4A2B-AD94-785B77BC15AA}.png)



## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
