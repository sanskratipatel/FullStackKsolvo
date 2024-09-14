# from django import forms
# from .models import Event
# from django.forms.widgets import DateTimeInput
#
#
# class EventForm(forms.ModelForm):
#     start_time = forms.DateTimeField(
#         widget=DateTimeInput(attrs={'type': 'datetime-local'}),
#         input_formats=['%Y-%m-%dT%H:%M']
#     )
#     end_time = forms.DateTimeField(
#         widget=DateTimeInput(attrs={'type': 'datetime-local'}),
#         input_formats=['%Y-%m-%dT%H:%M']
#     )
#
#     class Meta:
#         model = Event
#         fields = ['name', 'description', 'location', 'start_time', 'end_time']
#         widgets = {
#             'description': forms.Textarea(attrs={'rows': 4}),
#         }
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Event

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'location']
