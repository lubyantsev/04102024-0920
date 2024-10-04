from django.db import models

class Schedule(models.Model):
    password = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    schedule = models.ForeignKey(Schedule, related_name='events', on_delete=models.CASCADE)
    time = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    participant_name = models.CharField(max_length=255)