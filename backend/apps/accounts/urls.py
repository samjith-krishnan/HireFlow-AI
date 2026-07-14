from django.urls import path

from .views import RegisterCompanyAPIView,LoginAPIView

app_name = "accounts"

urlpatterns = [
    path("register/company/",RegisterCompanyAPIView.as_view(),name="register-company"),
    path("login/",LoginAPIView.as_view(),name="login"),
]