from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.companies.permissions import IsOwnerOrHR
from .serializers import CandidateSerializer
from .selectors import CandidateSelector
from .services import CandidateService


class CandidateListAPIView(generics.ListAPIView):
    serializer_class = CandidateSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrHR,
    ]

    def get_queryset(self):
        return CandidateSelector.list_candidates(
            self.request.user.company
        )


class CandidateRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = CandidateSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrHR,
    ]
    lookup_field = "id"

    def get_queryset(self):
        return CandidateSelector.list_candidates(
            self.request.user.company
        )

    def perform_update(self, serializer):
        CandidateService.update_candidate(serializer)

    def perform_destroy(self, instance):
        CandidateService.delete_candidate(instance)