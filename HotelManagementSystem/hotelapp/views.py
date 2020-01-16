from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

from rest_framework import generics


class HotelGuestView(generics.ListAPIView):
    serializer_class = Hotel_guestSerializers
    queryset = Hotel_Guest.objects.all()

class HotelGuestCreateView(generics.CreateAPIView):
    serializer_class = Hotel_guestSerializers
    queryset = Hotel_Guest.objects.all()

class HotelGuestUpdateView(generics.UpdateAPIView):
    serializer_class = Hotel_guestSerializers
    queryset = Hotel_Guest.objects.all()

class HotelGuestDestroyView(generics.DestroyAPIView):
    serializer_class = Hotel_guestSerializers
    queryset = Hotel_Guest.objects.all()



class RoomView(generics.ListAPIView):
    serializer_class = RoomSerializers
    queryset = Room.objects.all()

class RoomCreateView(generics.CreateAPIView):
    serializer_class = RoomSerializers
    queryset = Room.objects.all()

class RoomUpdateView(generics.UpdateAPIView):
    serializer_class = RoomSerializers
    queryset = Room.objects.all()

class RoomDeleteView(generics.DestroyAPIView):
    serializer_class = RoomSerializers
    queryset = Room.objects.all()

class ManagerView(generics.ListAPIView):
    serializer_class = ManagerSerializers
    queryset = Manager.objects.all()

class ManagerCreateView(generics.CreateAPIView):
    serializer_class = ManagerSerializers
    queryset = Manager.objects.all()

class ManagerUpdateView(generics.UpdateAPIView):
    serializer_class = ManagerSerializers
    queryset = Manager.objects.all()

class ManagerDeleteView(generics.DestroyAPIView):
    serializer_class = ManagerSerializers
    queryset = Manager.objects.all()