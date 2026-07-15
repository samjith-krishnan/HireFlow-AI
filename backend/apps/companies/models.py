
from django.db import models
from django.utils.text import slugify

from apps.common.models import BaseModel
from apps.common.choices import CompanySize


class Company(BaseModel):
  
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
    )

    website = models.URLField(
        blank=True,
    )

    logo = models.ImageField(
        upload_to="company/logos/",
        blank=True,
        null=True,
    )

    industry = models.CharField(
        max_length=100,
        blank=True,
    )

    company_size = models.CharField(
        max_length=20,
        choices=CompanySize.choices,
        default=CompanySize.SOLO,
    )

    address = models.TextField(
        blank=True,
    )

    city = models.CharField(
        max_length=100,
        blank=True,
    )

    state = models.CharField(
        max_length=100,
        blank=True,
    )

    country = models.CharField(
        max_length=100,
        blank=True,
    )

    timezone = models.CharField(
        max_length=100,
        default="UTC",
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "companies"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    


class Department(BaseModel):
    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="departments",
    )

    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "departments"
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["company", "name"],
                name="unique_department_per_company",
            )
        ]

    def __str__(self):
        return f"{self.company.name} - {self.name}"