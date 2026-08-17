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

    @staticmethod
    def extract_experience(text):
        if not text:
            return None

        patterns = [
            r"(\d+(?:\.\d+)?)\s*\+?\s*(?:years?|yrs?)\s*(?:of\s+)?experience",
            r"experience\s*(?:of|:|-)?\s*(\d+(?:\.\d+)?)\s*\+?\s*(?:years?|yrs?)",
        ]

        for pattern in patterns:
            match = re.search(
                pattern,
                text,
                re.IGNORECASE,
            )

            if match:
                return float(match.group(1))

        return None
    @staticmethod
    def extract_education(text):
        if not text:
            return []

        education_keywords = [
            "bca",
            "b.tech",
            "btech",
            "mca",
            "m.tech",
            "mtech",
            "b.sc",
            "bsc",
            "m.sc",
            "msc",
            "b.e",
            "be",
            "m.e",
            "me",
            "mba",
            "phd",
            "bachelor",
            "master",
            "doctorate",
        ]

        found_education = []

        text_lower = text.lower()

        for keyword in education_keywords:
            if keyword in text_lower:
                found_education.append(keyword)

        return found_education

    @staticmethod
    def extract(text):
        return {
            "skills": CandidateExtractorService.extract_skills(text),
            "experience_years": CandidateExtractorService.extract_experience(text),
            "education": CandidateExtractorService.extract_education(text),
            "projects": [],
        }