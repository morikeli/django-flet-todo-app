from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Task
import uuid

@receiver(pre_save, sender=Task)
def generate_taskID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4())

