from django.contrib import admin
from .models import Task, Note
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'assigned_by', 'title', 'description', 'complete', 'create']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'note', 'created_by']

