from django.contrib import admin
from .models import *

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'excerpt', 'primary_skill')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Redirect)