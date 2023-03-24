from django.db import models

class Task(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
    task = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task[:5]

    class Meta:
        ordering = ['-created']

