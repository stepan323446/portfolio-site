from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ProjectsListView.as_view()),
    path('detail/<slug:slug>', ProjectView.as_view())
]