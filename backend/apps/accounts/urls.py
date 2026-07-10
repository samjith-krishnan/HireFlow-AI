from django.urls import path

from .views import RegisterCompanyAPIView

app_name = "accounts"

urlpatterns = [
    path("register/company/",RegisterCompanyAPIView.as_view(),name="register-company"
    ),
]