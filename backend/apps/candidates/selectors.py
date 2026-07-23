from .models import Candidate


class CandidateSelector:

    @staticmethod
    def list_candidates(company):
        return Candidate.objects.filter(
            company=company,
            is_active=True,
        )

    @staticmethod
    def get_candidate(company, candidate_id):
        return Candidate.objects.get(
            company=company,
            id=candidate_id,
            is_active=True,
        )