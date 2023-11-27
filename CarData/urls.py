from django.urls import path
from .import views
from .views import ShowroomList

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('detail/<id>/', views.cardetail, name='car_detail'),
    path('car/edit/<id>/', views.car_detail_edit, name="edit"),
    path('car/change/<id>/', views.data_change, name="change"),
    path('car/delete/<id>/', views.remove_data, name="delete"),

    path('showroom/', ShowroomList.as_view(), name="showroom-list"),
    path('showroom/<int:id>/', views.Showroom_Detail.as_view(), name="showroom-detail"),

    path('review/', views.ReviewList.as_view(), name="review"),
    path('review/<int:id>/', views.ReviewDetail.as_view(), name='review-detail'),
    path('review/delete/<int:id>/', views.ReviewDelete.as_view(), name='review-delete')
]