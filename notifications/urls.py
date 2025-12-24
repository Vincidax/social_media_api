from django.urls import path
from .views import user_notifications

urlpatterns = [
    path('notifications/', user_notifications, name='notifications'),
]
