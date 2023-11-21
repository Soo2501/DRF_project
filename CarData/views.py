from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from .api_file.serializers import CarSerializers, ShowroomSerializers
from .models import Carlist, Showroomlist
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
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


@api_view(['GET','POST'])
def car_list(request):
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
        

@api_view(['GET','PATCH'])
def data_change(request, id):
    if request.method == "GET":
        car = Carlist.objects.get(id=id)
        serializer = CarSerializers(car)
        return Response(serializer.data)
    
    if request.method == "PATCH":
        car = Carlist.objects.get(id=id)
        serializer = CarSerializers(car,data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

@api_view(['GET','DELETE'])
def remove_data(request, id):
        car = Carlist.objects.get(id=id)
        car.delete()
        car_list = Carlist.objects.all()
        serializer = CarSerializers(car_list, many=True)
        return Response({'Payload':serializer.data,'messages':'deleted'})


class ShowroomList(APIView):
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    permission_classes = [IsAdminUser]


    def get(self, request):
        showroom = Showroomlist.objects.all()
        serializer = ShowroomSerializers(showroom, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ShowroomSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class Showroom_Detail(APIView):
    def get(self, request, id):
        try:
            showroom = Showroomlist.objects.get(id = id)
        except Showroomlist.DoesnotExist:
            return Response({'error' : 'not found'})
        serializer = ShowroomSerializers(showroom)
        return Response(serializer.data) 

    def put(self, request, id):
        showroom = Showroomlist.objects.get(id=id)
        serializer = ShowroomSerializers(showroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
        
    def delete(self, request, id):
        showroom = Showroomlist.objects.get(id=id)
        showroom.delete()
        return Response({'message': 'data deleted successfully'})