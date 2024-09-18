from rest_framework import serializers
from projects.serializers import ProjectSerializer
from .models import *

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

# Skill category for post
class SkillCategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = SkillCategory
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    
    class Meta:
        model = Education
        fields = '__all__'

class PrimaryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryBio
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

# Post
class FileSerializer(serializers.ModelSerializer):
    cats = SkillCategorySerializer(many=True, read_only=True)
    jobs = JobSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)

    class Meta:
        model = FileModel
        fields = '__all__'

# Sidebar
class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = ('title', 'slug', 'folder')

class FolderSerializer(serializers.ModelSerializer):
    files = FileListSerializer(many=True, read_only=True)
    
    class Meta:
        model = FolderModel
        fields = '__all__'