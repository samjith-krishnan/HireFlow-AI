class JobService:

    @staticmethod
    def create_job(serializer, company, created_by):
        serializer.save(
            company=company,
            created_by=created_by,
        )

    @staticmethod
    def update_job(serializer):
        serializer.save()

    @staticmethod
    def delete_job(job):
        job.is_active = False
        job.save(update_fields=["is_active"])