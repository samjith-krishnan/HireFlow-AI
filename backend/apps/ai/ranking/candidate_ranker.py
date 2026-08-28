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

        if (
            maximum_experience > 0
            and candidate_experience > maximum_experience
        ):
            return 100.0

        return 100.0


