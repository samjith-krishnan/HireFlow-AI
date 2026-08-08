from django.urls import path

from .views import PublicJobAPIView

app_name = "public"

urlpatterns = [
    path("jobs/<str:apply_token>/",PublicJobAPIView.as_view(),name="public-job-detail"),
]