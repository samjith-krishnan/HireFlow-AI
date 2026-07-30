from django.db import transaction
from django.utils import timezone

from .models import Application


class ApplicationService:

    @staticmethod
    @transaction.atomic
    def create_application(serializer):
        return serializer.save()

    @staticmethod
    @transaction.atomic
    def update_application(serializer):
        return serializer.save()

    @staticmethod
    @transaction.atomic
    def delete_application(application):
        application.delete()

    @staticmethod
    @transaction.atomic
    def change_status(application, status, reviewed_by=None):
        application.status = status

        if reviewed_by:
            application.reviewed_by = reviewed_by
            application.reviewed_at = timezone.now()

        application.save(
            update_fields=[
                "status",
                "reviewed_by",
                "reviewed_at",
                "updated_at",
            ]
        )

        return application