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