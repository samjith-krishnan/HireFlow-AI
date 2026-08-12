from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.companies.permissions import IsOwnerOrHR

from .serializers import ApplicationSerializer
from .selectors import ApplicationSelector
from .services import ApplicationService


class ApplicationListAPIView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrHR,
    ]

    def get_queryset(self):
        return ApplicationSelector.list_applications(
            self.request.user.company
        )


class ApplicationRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = ApplicationSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrHR,
    ]
    lookup_field = "id"

    def get_queryset(self):
        return ApplicationSelector.list_applications(
            self.request.user.company
        )

    def perform_update(self, serializer):
        ApplicationService.update_application(serializer)

    def perform_destroy(self, instance):
        ApplicationService.delete_application(instance)

