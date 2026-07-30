from .models import Application


class ApplicationSelector:

    @staticmethod
    def list_applications(company):
        return (
            Application.objects
            .filter(job__company=company)
            .select_related(
                "candidate",
                "job",
                "reviewed_by",
            )
        )

    @staticmethod
    def get_application(company, application_id):
        return (
            Application.objects
            .select_related(
                "candidate",
                "job",
                "reviewed_by",
            )
            .get(
                id=application_id,
                job__company=company,
            )
        )