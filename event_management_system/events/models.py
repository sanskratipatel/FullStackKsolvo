# from django.db import models
#
# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
#
# class Event(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     location = models.CharField(max_length=255)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     organizer = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#
# class Attendee(models.Model):
#     event = models.ForeignKey(Event, related_name='attendees', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     rsvp_status = models.BooleanField(default=False)
#     rsvp_at = models.DateTimeField(null=True, blank=True)
#
#     def __str__(self):
#         return f"{self.user.username} attending {self.event.name}"
#
# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     message = models.CharField(max_length=255)
#     is_read = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Notification for {self.user.username} for event {self.event.name}"
# class ActivityLog(models.Model):
#     # Define the fields for the ActivityLog model
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     action = models.CharField(max_length=255)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.user} - {self.action} - {self.timestamp}"

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from .models import ActivityLog

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(User, related_name='attendees', blank=True)

    def __str__(self):
        return self.name

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.user.username}'


class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    rsvp_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} attending {self.event.name}'


class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    activity = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.activity} on {self.timestamp}'


# @admin.register(ActivityLog)
# class ActivityLogAdmin(admin.ModelAdmin):
#     list_display = ('action', 'timestamp')