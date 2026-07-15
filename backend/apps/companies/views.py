from rest_framework import generics

from .models import Department
from .permissions import IsOwnerOrHR
from .serializers import DepartmentSerializer
from .services import DepartmentService
from .selectors import DepartmentSelector


class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [IsOwnerOrHR]

    def get_queryset(self):
        return DepartmentSelector.list_departments(
            company=self.request.user.company
        )

    def perform_create(self, serializer):
        DepartmentService.create_department(
            serializer,
            self.request.user.company,
        )


class DepartmentRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = DepartmentSerializer
    permission_classes = [IsOwnerOrHR]
    lookup_field = "id"

    def get_queryset(self):
        return DepartmentSelector.list_departments(
            company=self.request.user.company
        )

    def perform_update(self, serializer):
        DepartmentService.update_department(
            department=self.get_object(),
            validated_data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        DepartmentService.delete_department(
            department=instance
        )