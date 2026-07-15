from .models import Department


class DepartmentSelector:

    @staticmethod
    def list_departments(company):
        return Department.objects.filter(
            company=company,
            is_active=True,
        )

    @staticmethod
    def get_department(company, department_id):
        return Department.objects.get(
            company=company,
            id=department_id,
            is_active=True,
        )