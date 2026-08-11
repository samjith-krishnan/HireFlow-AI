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


class PublicApplySerializer(serializers.Serializer):

    first_name = serializers.CharField(
        max_length=100,
    )

    last_name = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
    )

    email = serializers.EmailField()

    phone_number = serializers.CharField(
        max_length=20,
        required=False,
        allow_blank=True,
    )

  
    resume = serializers.FileField()

    cover_letter = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    def validate_resume(self, value):
        allowed_extensions = (".pdf", ".doc", ".docx")

        if not value.name.lower().endswith(allowed_extensions):
            raise serializers.ValidationError(
                "Only PDF, DOC and DOCX files are allowed."
            )

        max_size = 5 * 1024 * 1024  

        if value.size > max_size:
            raise serializers.ValidationError(
                "Resume size must not exceed 5 MB."
            )

        return value