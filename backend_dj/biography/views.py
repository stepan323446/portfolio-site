from django.shortcuts import render
from rest_framework import generics as rest_generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status as rest_status

from .serializers import *

# Create your views here.
class SkillListView(rest_generics.ListAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()

# Skill categories like 'Frontend'
class SkillCategoryListView(rest_generics.ListAPIView):
    serializer_class = SkillCategorySerializer
    queryset = SkillCategory.objects.all()

# Contact list
class ContactView(rest_generics.ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.order_by('order')

# Common post
class FileView(rest_generics.RetrieveAPIView):
    serializer_class = FileSerializer
    queryset = FileModel.objects.all()
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

# Primary info in the sidebar
class PrimaryInfoView(APIView):
    def get(self, request, format=None):
        primaryBio = PrimaryBio.objects.first()

        if primaryBio == None:
            return Response({'error: Not found primary info'}, status=rest_status.HTTP_404_NOT_FOUND)
        
        primaryBioSerialized = PrimaryInfoSerializer(instance=primaryBio, context={'request': request})
        return Response(primaryBioSerialized.data)

# All posts
class FileListView(rest_generics.ListAPIView):
    serializer_class = FileSerializer
    queryset = FileModel.objects.order_by('order')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

# Sidebar
class SidebarBioView(APIView):
    def get(self, request, format=None):
        folders_queryset = FolderModel.objects.all()
        files_non_folder_queryset = FileModel.objects.filter(folder=None)

        folders = FolderSerializer(instance=folders_queryset, many=True)
        files_non_folder = FileListSerializer(instance=files_non_folder_queryset, many=True)

        return Response({
            'folders': folders.data,
            'files_non_folder': files_non_folder.data
        })