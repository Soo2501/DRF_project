from django.urls import path
from .import views

urlpatterns = [
    path('', views.carlist, name='car_list'),
    path('detail/<id>/', views.cardetail, name='detail'),
]