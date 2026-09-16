from django.db import transaction
from django.utils import timezone
from .models import Application
from rest_framework.exceptions import ValidationError
from apps.candidates.services import CandidateService
from .selectors import ApplicationSelector
from apps.ai.services import ResumeParserService
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


    @staticmethod
    @transaction.atomic
    def create_application(
        *,
        job,
        first_name,
        last_name,
        email,
        phone_number,
        resume,
        cover_letter,
    ):
        candidate = CandidateService.get_or_create_candidate(
            company=job.company,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
        )

        if ApplicationSelector.has_applied(
            candidate=candidate,
            job=job,
        ):
            raise ValidationError(
                "You have already applied for this job."
            )

        application = Application.objects.create(
            candidate=candidate,
            job=job,
            resume=resume,
            cover_letter=cover_letter,
        )
        ResumeParserService.process_application(application)

        return application