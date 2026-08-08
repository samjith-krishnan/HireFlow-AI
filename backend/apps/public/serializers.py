from rest_framework import serializers

from apps.jobs.models import Job


class PublicJobSerializer(serializers.ModelSerializer):
    company = serializers.CharField(
        source="company.name",
        read_only=True,
    )

    skills = serializers.StringRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Job
        fields = (
            "title",
            "company",
            "description",
            "responsibilities",
            "requirements",
            "location",
            "employment_type",
            "minimum_experience",
            "maximum_experience",
            "minimum_salary",
            "maximum_salary",
            "vacancies",
            "deadline",
            "is_remote",
            "skills",
        )