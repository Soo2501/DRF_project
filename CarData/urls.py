from django.urls import path
from .import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('detail/<id>/', views.cardetail, name='detail'),
    path('car/edit/<id>/', views.car_detail_edit, name="edit"),
    path('car/change/<id>/', views.data_change, name="change"),
    path('car/delete/<id>/', views.remove_data, name="delete"),
]