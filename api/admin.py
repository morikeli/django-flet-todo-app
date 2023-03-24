from django.contrib import admin
from .models import Task

@admin.register(Task)
class TasksTable(admin.ModelAdmin):
    list_display = ['task', 'created']

