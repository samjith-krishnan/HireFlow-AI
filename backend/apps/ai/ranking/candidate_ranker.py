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