from django.db import router
from django.urls import path,include
from .views import *

#  HotelGuestView,HotelGuestCreateView,HotelGuestUpdateView,HotelGuestDestroyView, RoomView, ManagerView



urlpatterns=[
    path('hotel/',HotelGuestView.as_view(),name='hotel'),
    path('hotel/add/',HotelGuestCreateView.as_view(),name='hotel create'),
    path('hotel/update/',HotelGuestUpdateView.as_view(),name='hotel update'),
    path('hotel/delete/',HotelGuestDestroyView.as_view(),name='hotel Delete'),
    path('room', RoomView.as_view(), name='room'),
    path('room/add/',RoomCreateView.as_view(),name='room create'),
    path('room/update/',RoomUpdateView.as_view(),name='room update'),
    path('room/delete/',RoomDeleteView.as_view(),name='room Delete'),
    path('manager', ManagerView.as_view(), name='manager'),
    path('manager/add/',ManagerCreateView.as_view(),name='manager create'),
    path('manager/update/',ManagerUpdateView.as_view(),name='manager update'),
    path('manager/delete/',ManagerDeleteView.as_view(),name='manager Delete'),


]




