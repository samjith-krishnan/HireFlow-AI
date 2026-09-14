from apps.ai.ranking.candidate_ranker import CandidateRanker


class CandidateRanker:

    @staticmethod
    def calculate_skill_score(
        required_skills,
        candidate_skills,
    ):
        if not required_skills:
            return 100.0

        required = {
            skill.lower().strip()
            for skill in required_skills
        }

        candidate = {
            skill.lower().strip()
            for skill in candidate_skills
        }

        matched_skills = required.intersection(candidate)

        return (
            len(matched_skills) / len(required)
        ) * 100

    @staticmethod
    def calculate_experience_score(
        minimum_experience,
        maximum_experience,
        candidate_experience,
    ):
        if candidate_experience is None:
            return 0.0

        if candidate_experience < minimum_experience:
            if minimum_experience == 0:
                return 100.0

            return (
                candidate_experience / minimum_experience
            ) * 100

        return 100.0

    @staticmethod
    def calculate_score(
        required_skills,
        candidate_skills,
        minimum_experience,
        maximum_experience,
        candidate_experience,
    ):
        skill_score = CandidateRanker.calculate_skill_score(
            required_skills,
            candidate_skills,
        )

        experience_score = CandidateRanker.calculate_experience_score(
            minimum_experience,
            maximum_experience,
            candidate_experience,
        )

        final_score = (
            skill_score * 0.60
            + experience_score * 0.40
        )

        return round(final_score, 2)

    @staticmethod
    def rank_application(application):

        job = application.job

        required_skills = list(
            job.skills.values_list(
                "name",
                flat=True
            )
        )

        parsed_data = application.parsed_data or {}

        candidate_skills = parsed_data.get(
            "skills",
            []
        )

        candidate_experience = parsed_data.get(
            "experience_years"
        )

        score = CandidateRanker.calculate_score(
            required_skills=required_skills,
            candidate_skills=candidate_skills,
            minimum_experience=job.minimum_experience,
            maximum_experience=job.maximum_experience,
            candidate_experience=candidate_experience,
        )

        application.ai_score = score

        application.save(
            update_fields=["ai_score"]
        )

        return score