from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel


class Message(TimeStampedModel):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
