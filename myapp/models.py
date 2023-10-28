from django.db import models
from django.utils import timezone


class Appointment(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.IntegerField()
    pet = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=200)
    selected_service = models.CharField(max_length=200)
