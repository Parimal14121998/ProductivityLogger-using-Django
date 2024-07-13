from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime


class WorkSession(models.Model):
    task = models.ForeignKey('Task', related_name='work_sessions', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)

    def duration(self):
        if self.end_time:
            return self.end_time - self.start_time
        return timedelta()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    time_limit = models.DurationField(default=timedelta(hours=8))  # Default time limit
    time_exceeded = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def total_working_hours(self):
        total_duration = timedelta()
        for session in self.work_sessions.all():
            total_duration += session.duration()
        return total_duration

    def save(self, *args, **kwargs):
        if self.completed:
            actual_working_hours = self.total_working_hours()
            self.time_exceeded = actual_working_hours > self.time_limit
        super().save(*args, **kwargs)
