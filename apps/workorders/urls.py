
from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkOrderList.as_view(), name='work_order_list'),
    path('<int:work_order_id>', views.WorkOrderDetail.as_view(), name='work_order_detail'),
    path('items/', views.WorkOrderItemList.as_view(), name='work_order_item_list'),
    path('items/<int:work_order_item_id>', views.WorkOrderItemDetail.as_view(), name='work_order_item_detail'),
]
