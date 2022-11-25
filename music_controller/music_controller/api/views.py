# Example------------------
# from django.http import HttpResponse
# Create your views here.

# def main (request):
#     return HttpResponse("<h1>Hello</h1>")

# def home(request):
#     return HttpResponse("<h2>home</h2>")

# def about(request):
#     return HttpResponse("<h3>about</h3>")
# ---------------------------------------
from django.shortcuts import render
from rest_framework import generics 
from .serializers import RoomSerializer
from .models import Room

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class= RoomSerializer