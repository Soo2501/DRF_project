from django.shortcuts import render
from django.http import JsonResponse
from .models import Carlist
# Create your views here.

def carlist(request):
    car = Carlist.objects.all()
    data = {
        'car' : list(car.values()),
    }
    return JsonResponse(data)

def cardetail(request, id):
    car = Carlist.objects.get(id=id)
    data = {
        'name' : car.name,
        'description' : car.description,
        'status' : car.active
    }
    return JsonResponse(data)