from .models import Candidate


class CandidateService:

    @staticmethod
    def get_or_create_candidate(
        company,
        validated_data,
    ):
        candidate, _ = Candidate.objects.get_or_create(
            company=company,
            email=validated_data["email"].lower().strip(),
            defaults=validated_data,
        )
        return candidate

    @staticmethod
    def update_candidate(serializer):
        serializer.save()

    @staticmethod
    def delete_candidate(candidate):
        candidate.is_active = False
        candidate.save(update_fields=["is_active"])