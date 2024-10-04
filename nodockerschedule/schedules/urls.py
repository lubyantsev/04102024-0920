from django.urls import path
from .views import home_view, create_event_view, open_schedule

urlpatterns = [
    path('', home_view, name='home'),
    path('create_event/<int:schedule_id>/', create_event_view, name='create_event'),
    path('open_schedule/', open_schedule, name='open_schedule'),]