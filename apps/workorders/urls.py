
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PartList.as_view(), name='part_list'),
    path('<int:part_id>', views.PartDetail.as_view(), name='part_detail'),
    path('oils/', views.OilList.as_view(), name='oil_list'),
    path('oils/<int:oil_id>', views.OilDetail.as_view(), name='oil_detail'),
    path('oil_containers/', views.OilContainerList.as_view(), name='oil_container_list'),
    path('works/', views.WorkList.as_view(), name='work_list'),
    path('works/<int:works_id>', views.WorkDetail.as_view(), name='work_detail'),
    path('kit_services/', views.KitServiceList.as_view(), name='kit_service_list'),
    path('kit_services/<int:kit_service_id>', views.KitServiceDetail.as_view(), name='kit_service_detail'),
]
