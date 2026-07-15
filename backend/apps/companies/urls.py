from django.urls import path

from .views import (
    DepartmentListCreateAPIView,
    DepartmentRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path(
        "departments/",
        DepartmentListCreateAPIView.as_view(),
        name="department-list-create",
    ),
    path(
        "departments/<uuid:id>/",
        DepartmentRetrieveUpdateDestroyAPIView.as_view(),
        name="department-detail",
    ),
]