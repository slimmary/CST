
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientProfileList.as_view(), name='client_profile_list'),
    path('<int:client_profile_id>', views.ClientProfileDetail.as_view(), name='client_profile'),

]
