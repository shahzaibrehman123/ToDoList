from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.


class Task(models.Model):
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name="assigned_by_user_in_task")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_in_task")
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']


class Note(models.Model):
    name = models.CharField(max_length=50, null=True)
    note = RichTextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="note_by_user")

    def __str__(self):
        return self.note


