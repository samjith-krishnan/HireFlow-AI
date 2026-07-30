from django.urls import path

from .views import (
    ApplicationListAPIView,
    ApplicationRetrieveUpdateDestroyAPIView,
)

app_name = "applications"

urlpatterns = [
    path("",ApplicationListAPIView.as_view(),name="application-list"),
    path("<uuid:id>/",ApplicationRetrieveUpdateDestroyAPIView.as_view(),name="application-detail"),
]