from django.db import models

from apps.common.models import BaseModel


class Employee(BaseModel):
    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="employee_profile",
    )

    employee_id = models.CharField(
        max_length=30,
        unique=True,
    )

    department = models.ForeignKey(
    "companies.Department",
    on_delete=models.SET_NULL,
    related_name="users",
    null=True,
    blank=True,
    )

    designation = models.CharField(
    max_length=100,
    blank=True,
      )

    joined_date = models.DateField()

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "employees"