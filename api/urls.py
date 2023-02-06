from django.urls import path
from .views import Track
urlpatterns=[
    path("track/",Track.as_view())
]