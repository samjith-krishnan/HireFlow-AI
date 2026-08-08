from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = (
            "id",
            "department",
            "title",
            "slug",
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
            "status",
            "skills",
            "is_remote",
            "is_featured",
            "is_active",
        )
        read_only_fields = (
            "id",
            "slug",
        )

    def validate(self, attrs):
        min_exp = attrs.get(
            "minimum_experience",
            getattr(self.instance, "minimum_experience", 0),
        )
        max_exp = attrs.get(
            "maximum_experience",
            getattr(self.instance, "maximum_experience", 0),
        )

        if min_exp > max_exp:
            raise serializers.ValidationError(
                {
                    "maximum_experience":
                    "Maximum experience must be greater than or equal to minimum experience."
                }
            )

        min_salary = attrs.get(
            "minimum_salary",
            getattr(self.instance, "minimum_salary", 0),
        )
        max_salary = attrs.get(
            "maximum_salary",
            getattr(self.instance, "maximum_salary", 0),
        )

        if min_salary > max_salary:
            raise serializers.ValidationError(
                {
                    "maximum_salary":
                    "Maximum salary must be greater than or equal to minimum salary."
                }
            )

        return attrs
    


class JobListSerializer(serializers.ModelSerializer):

    company = serializers.CharField(source="company.name")
    department = serializers.CharField(source="department.name")

    created_by = serializers.CharField(
        source="created_by.full_name"
    )

    class Meta:
        model = Job
        fields = (
            "id",
            "title",
            "company",
            "department",
            "employment_type",
            "location",
            "status",
            "deadline",
            "created_by",
            "created_at",
            "apply_token"
        )