from .models import Candidate


class CandidateService:

    @staticmethod
    def get_or_create_candidate(
        *,
        company,
        first_name,
        last_name,
        email,
        phone_number,
    ):
        candidate, created = Candidate.objects.get_or_create(
            company=company,
            email=email.lower().strip(),
            defaults={
                "first_name": first_name,
                "last_name": last_name,
                "phone_number": phone_number,
            },
        )

        return candidate

    @staticmethod
    def update_candidate(serializer):
        serializer.save()

    @staticmethod
    def delete_candidate(candidate):
        candidate.is_active = False
        candidate.save(update_fields=["is_active"])