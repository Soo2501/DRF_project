from django.urls import path
from .import views

urlpatterns = [
    path('', views.carlist, name='car_list'),
    path('add/', views.add_car, name='addcar'),
    path('detail/<id>/', views.cardetail, name='detail'),
    path('car/edit/<id>/', views.car_detail_edit, name="edit"),
]