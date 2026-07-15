from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from companies.permissions import IsOwnerOrHR
from .serializers import SkillSerializer
from .selectors import SkillSelector
from .services import SkillService


class SkillListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrHR]

    def get_queryset(self):
        return SkillSelector.list_skills()

    def perform_create(self, serializer):
        SkillService.create_skill(serializer)


class SkillRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrHR]
    lookup_field = "id"

    def get_queryset(self):
        return SkillSelector.list_skills()

    def perform_update(self, serializer):
        SkillService.update_skill(serializer)

    def perform_destroy(self, instance):
        SkillService.delete_skill(instance)