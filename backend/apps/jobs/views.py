from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.companies.permissions import IsOwnerOrHR
from .serializers import (
    JobSerializer,
    JobListSerializer,
)
from .selectors import JobSelector
from .services import JobService


class JobListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrHR,
    ]

    def get_queryset(self):
        return JobSelector.list_jobs(
            self.request.user.company
        )

    def get_serializer_class(self):
        if self.request.method == "GET":
            return JobListSerializer
        return JobSerializer

    def perform_create(self, serializer):
        JobService.create_job(
            serializer=serializer,
            company=self.request.user.company,
            created_by=self.request.user,
        )


class JobRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrHR,
    ]
    lookup_field = "id"

    def get_queryset(self):
        return JobSelector.list_jobs(
            self.request.user.company
        )

    def get_serializer_class(self):
        if self.request.method == "GET":
            return JobListSerializer
        return JobSerializer

    def perform_update(self, serializer):
        JobService.update_job(serializer)

    def perform_destroy(self, instance):
        JobService.delete_job(instance)