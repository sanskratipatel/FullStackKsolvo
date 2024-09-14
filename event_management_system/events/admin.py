from django.contrib import admin
from .models import Event, Attendee, Notification, ActivityLog

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'organizer', 'start_time', 'end_time', 'created_at')
    search_fields = ('name', 'description', 'location', 'organizer__username')
    list_filter = ('start_time', 'end_time', 'created_at')

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'rsvp_status', 'rsvp_at')
    search_fields = ('user__username', 'event__name')
    list_filter = ('rsvp_status',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'message', 'is_read', 'created_at')
    search_fields = ('user__username', 'event__name', 'message')
    list_filter = ('is_read',)

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    search_fields = ('user__username', 'action')
    list_filter = ('timestamp',)
