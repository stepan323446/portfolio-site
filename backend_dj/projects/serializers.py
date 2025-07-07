from rest_framework import serializers
from .models import Project, Contributor
from biography.models import Skill


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectListSerializer(serializers.ModelSerializer):
    primary_skill = SkillSerializer()
    contributors = ContributorSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'slug', 'type', 'background', 'primary_skill', 'skills', 'excerpt', 'contributors')

class ProjectSerializer(serializers.ModelSerializer):
    primary_skill = SkillSerializer()
    skills = SkillSerializer(many=True)
    contributors = ContributorSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'