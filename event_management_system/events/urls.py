from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from events import views as event_views

# from events.views import notification_list

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    # path('signup/', views.signup_view, name='signup'),
    path(' ', event_views.list_events, name='home'),
    path('event/<int:id>/', views.event_detail, name='event_detail'),
    path('create_event/', views.create_event, name='create_event'),
    path('notifications/', views.view_notifications, name='notifications'),
]
