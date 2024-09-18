from django.urls import path
from .views import *

urlpatterns = [
    path('skill-list/', SkillListView.as_view()),
    path('skill-category-list/', SkillCategoryListView.as_view()),
    path('primary-info/', PrimaryInfoView.as_view()),
    path('contacts/', ContactView.as_view()),
    path('file/<slug:slug>', FileView.as_view()),
    path('file-list/', FileListView.as_view()),
]