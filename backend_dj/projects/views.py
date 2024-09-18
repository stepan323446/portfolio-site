from django.shortcuts import render
from rest_framework import generics as rest_generics
from .models import *
from .serializers import *

import time
# Create your views here.

class ProjectsListView(rest_generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ProjectView(rest_generics.RetrieveAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


