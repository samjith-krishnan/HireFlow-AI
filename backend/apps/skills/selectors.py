from .models import Skill

class SkillSelector:

    @staticmethod
    def list_skills():
        return Skill.objects.filter(
            is_active=True
        )

    @staticmethod
    def get_skill(skill_id):
        return Skill.objects.get(
            id=skill_id,
            is_active=True,
        )