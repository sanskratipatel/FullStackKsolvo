from django.core.mail import send_mail
from django.conf import settings
from .models import Notification, ActivityLog


def send_event_reminder(event, attendee):
    """
    Sends an email reminder to the attendee and creates an in-app notification.
    """
    subject = f"Reminder: {event.name}"
    message = f"""Hi {attendee.user.username},

This is a reminder for the event '{event.name}' scheduled on {event.start_time} at {event.location}.

Description: {event.description}

Best Regards,
Event Management Team
"""
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [attendee.user.email],
        fail_silently=False,
    )

    # Create in-app notification
    Notification.objects.create(
        user=attendee.user,
        event=event,
        message=f"Reminder: '{event.name}' is scheduled on {event.start_time} at {event.location}."
    )

    # Log the activity
    log_user_activity(attendee.user, f"Received reminder for event '{event.name}'")


def log_user_activity(user, action):
    """
    Logs a user activity.
    """
    ActivityLog.objects.create(user=user, action=action)
