// Toggle password visibility
ImportError: cannot import name 'Attendee' from 'events.models'

function togglePassword() {
    var passwordField = document.getElementById("password");
    if (passwordField.type === "password") {
        passwordField.type = "text";
    } else {
        passwordField.type = "password";
    }
}

// Example function for reminders
function sendReminder(eventId) {
    // Send reminder notification
    alert("Reminder sent for event ID: " + eventId);
}

