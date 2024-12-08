from django.contrib import admin
from .models import PersonalInfo, Project, Technology

admin.site.register(PersonalInfo)
admin.site.register(Project)
admin.site.register(Technology)