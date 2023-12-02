from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from .api_file.serializers import CarSerializers, ShowroomSerializers, ReviewSerializers
from .models import Carlist, Showroomlist, Review
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions, IsAuthenticatedOrReadOnly
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from .api_file.permissions import AdminOrReadOnlyPermissions, ReviewUserOrReadOnlyPermissions

"""
Using ListApiView
"""
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializers
    def get_queryset(self):
        return Review.objects.all()


    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        cars = get_object_or_404(Carlist, pk=pk)
        useredit = self.request.user
        Review_queryset = Review.objects.filter(car=cars, apiuser=useredit)
        if Review_queryset.exists():
            raise ValidationError("You have already reviewed this car")
        serializer.save(car=cars, apiuser=useredit)
        

class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializers
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(car=pk)
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    authentication_classes = [TokenAuthentication]
    # permission_classes = [AdminOrReadOnlyPermissions]
    permission_classes = [ReviewUserOrReadOnlyPermissions]

# class ReviewList(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializers

# class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializers
#     lookup_field = 'id'


# class ReviewList(mixins.ListModelMixin, 
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializers
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [DjangoModelPermissions]

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class ReviewDetail(mixins.RetrieveModelMixin, 
#                    generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializers
#     lookup_field = 'id'

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
# class ReviewDelete(mixins.DestroyModelMixin,
#                    generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializers
#     lookup_field = 'id'

#     def get(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)




# Create your views here.

# def carlist(request):
#     car = Carlist.objects.all()
#     data = {
#         'car':list(car.values()),
#     }

#     return JsonResponse(data)


# def cardetail(request, id):
#     car = Carlist.objects.get(pk=id)
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
def cardetail(request, pk):
    car = Carlist.objects.get(pk=pk)
    serializer = CarSerializers(car)

    return Response(serializer.data)


@api_view(['GET','PUT'])
def car_detail_edit(request, pk):
    if request.method == "GET":
        car = Carlist.objects.get(pk=pk)
        serializer = CarSerializers(car)
        return Response(serializer.data)


    if request.method == "PUT":
        car = Carlist.objects.get(pk=id)
        serializer = CarSerializers(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
        

@api_view(['GET','PATCH'])
def data_change(request, id):
    if request.method == "GET":
        car = Carlist.objects.get(pk=id)
        serializer = CarSerializers(car)
        return Response(serializer.data)
    
    if request.method == "PATCH":
        car = Carlist.objects.get(pk=id)
        serializer = CarSerializers(car,data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

@api_view(['GET','DELETE'])
def remove_data(request, id):
        car = Carlist.objects.get(pk=id)
        car.delete()
        car_list = Carlist.objects.all()
        serializer = CarSerializers(car_list, many=True)
        return Response({'Payload':serializer.data,'messages':'deleted'})


"""
    Using Viewset
"""
# class Showroom_Viewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Showroomlist.objects.all()
#         serializer = ShowroomSerializers(queryset, many=True)
#         return Response(serializer.data)
    

#     def retrieve(self, request, pk=None):
#         queryset = Showroomlist.objects.all()
#         showroom = get_object_or_404(queryset, pk=pk)
#         serializer = ShowroomSerializers(showroom)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = ShowroomSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     def destroy(self, request, pk=None):
#         queryset = Showroomlist.objects.all()
#         showroom = get_object_or_404(queryset, pk=pk)
#         showroom.delete()
#         return Response({"message":"data deleted successfully"})


"""Using ModelViewset"""

# class Showroom_ViewSet(viewsets.ModelViewSet):
class Showroom_ViewSet(viewsets.ReadOnlyModelViewSet):
    """
        A simple ViewSet for viewing and editing accounts.
    """
    queryset = Showroomlist.objects.all()
    serializer_class = ShowroomSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]



class ShowroomList(APIView):
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [SessionAuthentication]
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
        showroom = Showroomlist.objects.get(pk=id)
        serializer = ShowroomSerializers(showroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
        
    def delete(self, request, id):
        showroom = Showroomlist.objects.get(pk=id)
        showroom.delete()
        return Response({'message': 'data deleted successfully'})
    
