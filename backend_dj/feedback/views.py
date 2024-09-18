from rest_framework import generics as rest_generics
from django.shortcuts import render
from .serializers import MessageSerializer
import time

# Create your views here.
class CreateMessageView(rest_generics.CreateAPIView):
    serializer_class = MessageSerializer
    
    def post(self, request, *args, **kwargs):
        time.sleep(5)
        return super().post(request, *args, **kwargs)