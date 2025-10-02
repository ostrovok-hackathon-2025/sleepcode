from django.urls import path
from .views import hotel_list

urlpatterns = [path("", hotel_list, name="hotel_list")]
