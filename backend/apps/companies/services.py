from .models import Department

class DepartmentService:

    @staticmethod
    def create_department(serializer, company):
        serializer.save(company=company)

    @staticmethod
    def update_department(serializer):
        serializer.save()

    @staticmethod
    def delete_department(department):
        department.is_active = False
        department.save(update_fields=["is_active"])