from django.shortcuts import render
from django.contrib.auth.models import User 
from rest_framework import generics 
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() #list of objects
    serializer_class = UserSerializer #tells the view the kind of data to expect when creating a new user
    permission_classes = [AllowAny] #this class specifies who can call this view 
    
