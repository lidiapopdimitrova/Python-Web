from django.contrib import admin

from django_introduction.tasks.models import Task


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
