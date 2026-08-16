import re

from apps.skills.models import Skill


class CandidateExtractorService:

    @staticmethod
    def extract_skills(text):
        if not text:
            return []

        matched_skills = []

        for skill in Skill.objects.all():
            skill_name = skill.name.strip()

            pattern = rf"(?<!\w){re.escape(skill_name)}(?!\w)"

            if re.search(pattern, text, re.IGNORECASE):
                matched_skills.append(skill_name)

        return matched_skills