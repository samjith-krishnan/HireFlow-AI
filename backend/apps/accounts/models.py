from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.common.models import BaseModel
from apps.common.choices import UserRole
from .managers import UserManager


class User(BaseModel, AbstractUser):

    company = models.ForeignKey(
                "companies.Company",
                on_delete=models.CASCADE,
                default="",
                null=True,
                blank=True,
            )

    username = None
    email = models.EmailField(
        unique=True,
    )

    first_name = models.CharField(
        max_length=100,
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
    )

    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.HR,
    )
    is_verified = models.BooleanField(
        default=False,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "users"
        ordering = ["-created_at"]

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
    

