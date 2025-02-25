from django.contrib import admin
from .models import Professor, Module, Instance, Student, Rating

# Register your models here.

admin.site.register(Professor)
admin.site.register(Module)
admin.site.register(Instance)
admin.site.register(Student)
admin.site.register(Rating)