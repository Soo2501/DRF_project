from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .api_file.serializers import CarSerializers
from .models import Carlist
# Create your views here.

# def carlist(request):
#     car = Carlist.objects.all()
#     data = {
#         'car':list(car.values()),
#     }

#     return JsonResponse(data)


# def cardetail(request, id):
#     car = Carlist.objects.get(id=id)
#     data = {
#         'name' : car.name,
#         'description' : car.description,
#         'status' : car.active
#     }
#     return JsonResponse(data)


@api_view(["GET"])
def carlist(request):
    car = Carlist.objects.all()

    serializer = CarSerializers(car,many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def add_car(request):
    if request.method == "GET":
        car = Carlist.objects.all()
        serializer = CarSerializers(car,many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = CarSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET'])
def cardetail(request, id):
    car = Carlist.objects.get(id=id)
    serializer = CarSerializers(car)

    return Response(serializer.data)


@api_view(['GET','PUT'])
def car_detail_edit(request, id):
    if request.method == "GET":
        car = Carlist.objects.get(id=id)
        serializer = CarSerializers(car)
        return Response(serializer.data)


    if request.method == "PUT":
        car = Carlist.objects.get(id=id)
        serializer = CarSerializers(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)