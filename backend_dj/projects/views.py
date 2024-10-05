from django.http import HttpRequest
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.generic import ListView
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

class RedirectAllView(ListView):
    model = Redirect
    context_object_name = 'redirects'
    template_name = 'projects/redirect.html'


def redirect_view(request: HttpRequest, name: str):
    try:
        redirect_obj = Redirect.objects.get(name=name)
        return redirect(redirect_obj.url)
    except:
        return redirect(reverse('redirect-index'))

        
