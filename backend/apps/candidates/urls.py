from django.urls import path

from .views import (
    CandidateListAPIView,
    CandidateRetrieveUpdateDestroyAPIView,
)

app_name = "candidates"

urlpatterns = [
    path("",CandidateListAPIView.as_view(),name="candidate-list"),
    path("<uuid:id>/",CandidateRetrieveUpdateDestroyAPIView.as_view(),name="candidate-detail"),
]