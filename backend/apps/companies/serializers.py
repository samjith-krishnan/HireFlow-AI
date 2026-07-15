from rest_framework import serializers

from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = (
            "id",
            "name",
            "description",
            "is_active",
        )

    def validate_name(self, value):
        company = self.context["request"].user.company

        queryset = Department.objects.filter(
            company=company,
            name__iexact=value,
        )

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                "Department with this name already exists."
            )

        return value