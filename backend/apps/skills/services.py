class SkillService:

    @staticmethod
    def create_skill(serializer):
        serializer.save()

    @staticmethod
    def update_skill(serializer):
        serializer.save()

    @staticmethod
    def delete_skill(skill):
        skill.is_active = False
        skill.save(update_fields=["is_active"])