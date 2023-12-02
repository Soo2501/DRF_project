from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
from .views import ShowroomList

router = DefaultRouter()
# router.register('showroom', views.Showroom_Viewset, basename='showroom')
router.register('showroom', views.Showroom_ViewSet, basename='showroom')

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('detail/<pk>/', views.cardetail, name='car_detail'),
    path('car/edit/<pk>/', views.car_detail_edit, name="edit"),
    path('car/change/<pk>/', views.data_change, name="change"),
    path('car/delete/<pk>/', views.remove_data, name="delete"),

    # path('showroom/', ShowroomList.as_view(), name="showroom-list"),
    # path('showroom/<int:id>/', views.Showroom_Detail.as_view(), name="showroom-detail"),
    path('', include(router.urls)),

    # path('review/', views.ReviewList.as_view(), name="review"),
    # path('review/<int:id>/', views.ReviewDetail.as_view(), name='review-detail'),
    # path('review/delete/<int:id>/', views.ReviewDelete.as_view(), name='review-delete')

    path('showroom/<int:pk>/review-create/', views.ReviewCreate.as_view(), name="review_create"),
    path('showroom/<int:pk>/review/', views.ReviewList.as_view(), name='review_list'),
    path('showroom/review/<int:pk>/', views.ReviewDetail.as_view(), name='review_detail'),


]