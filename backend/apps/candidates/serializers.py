from rest_framework import serializers

from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "linkedin_url",
            "github_url",
            "portfolio_url",
            "location",
            "is_active",
        )
        read_only_fields = ("id",)