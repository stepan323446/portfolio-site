from rest_framework import serializers
from .models import Project
from biography.models import Skill



class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectListSerializer(serializers.ModelSerializer):
    primary_skill = SkillSerializer()
    class Meta:
        model = Project
        fields = ('id', 'title', 'slug', 'type', 'background', 'primary_skill', 'skills', 'excerpt')

class ProjectSerializer(serializers.ModelSerializer):
    primary_skill = SkillSerializer()
    skills = SkillSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'