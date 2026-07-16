from django.urls import path

from .views import (
    JobListCreateAPIView,
    JobRetrieveUpdateDestroyAPIView,
)

app_name = "jobs"

urlpatterns = [
    path("",JobListCreateAPIView.as_view(),name="job-list-create"),
    path("<uuid:id>/",JobRetrieveUpdateDestroyAPIView.as_view(),name="job-detail"),
]