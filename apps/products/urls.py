
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DetailList.as_view(), name='detail_list'),
    path('<int:detail_id>', views.DetailDetail.as_view(), name='detail_dateil'),
    path('oils/', views.OilList.as_view(), name='oil_list'),
    path('oils/<int:oil_id>', views.OilDetail.as_view(), name='oil_detail'),
    path('oil_containers/', views.OilContainerList.as_view(), name='oil_container_list'),
    path('services/', views.ServiceList.as_view(), name='service_list'),
    path('services/<int:service_id>', views.ServiceDetail.as_view(), name='service_detail'),
    path('kit_services/', views.KitServiceList.as_view(), name='kit_service_list'),
    path('kit_services/<int:kit_service_id>', views.KitServiceDetail.as_view(), name='kit_service_detail'),
]
