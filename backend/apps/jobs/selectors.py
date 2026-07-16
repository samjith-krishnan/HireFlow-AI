from .models import Job


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