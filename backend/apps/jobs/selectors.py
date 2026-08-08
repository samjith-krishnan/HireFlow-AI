from .models import Job
from django.shortcuts import get_object_or_404
from apps.common.choices import JobStatus


class JobSelector:

    @staticmethod
    def list_jobs(company):
        return (
            Job.objects.filter(
                company=company,
                is_active=True,
            )
            .select_related(
                "company",
                "department",
                "created_by",
            )
            .prefetch_related(
                "skills",
            )
        )

    @staticmethod
    def get_job(company, job_id):
        return Job.objects.get(
            company=company,
            id=job_id,
            is_active=True,
        )

    @staticmethod
    def get_public_job(apply_token):
        return get_object_or_404(
            Job.objects.select_related(
                "company",
            ).prefetch_related(
                "skills",
            ),
            apply_token=apply_token,
            is_active=True,
            status=JobStatus.OPEN,
        )