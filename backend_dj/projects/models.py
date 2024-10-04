from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from biography.models import Skill

# Create your models here.
class Project(models.Model):
    title       = models.CharField(max_length=150, verbose_name="Title")
    slug        = models.SlugField(max_length=150, db_index=True, unique=True, verbose_name="Slug")
    type        = models.CharField(max_length=150, verbose_name="Type project")
    date_created = models.DateField()
    background  = models.ImageField(upload_to="uploads/")
    content     = RichTextUploadingField(blank=True, verbose_name="Content")
    excerpt     = models.TextField(blank=True, null=True)
    primary_skill = models.ForeignKey(Skill, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Primary skill", related_name="primary_skill")
    skills      = models.ManyToManyField(Skill, verbose_name="Skills")

    code_url    = models.CharField(max_length=150, null=True, blank=True, verbose_name="View code URL")
    run_url     = models.CharField(max_length=150, null=True, blank=True, verbose_name="Run URL")

    @property
    def get_photo_url(self):
        return self.background.url

    def __str__(self):
       return self.title
    
class Redirect(models.Model):
    name        = models.CharField(max_length=150)
    url         = models.URLField()

    def __str__(self) -> str:
        return self.name