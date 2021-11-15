
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarList.as_view(), name='car_list'),
    path('cars', views.CarList.as_view(), name='car_list'),
    path('<int:car_id>', views.CarDetail.as_view(), name='car_detail'),
    path('brandmodel', views.BrandModelList.as_view(), name='brand_model_list'),
    path('brandmodel/<int:brandmodel_id>', views.BrandModelDetail.as_view(), name='brand_model_detail'),
]
