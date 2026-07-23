from django.db import models

from apps.common.models import BaseModel


class Candidate(BaseModel):
    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="candidates",
    )

    first_name = models.CharField(
        max_length=100,
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
    )

    email = models.EmailField()

    phone_number = models.CharField(
        max_length=20,
        blank=True,
    )

    linkedin_url = models.URLField(
        blank=True,
    )

    github_url = models.URLField(
        blank=True,
    )

    portfolio_url = models.URLField(
        blank=True,
    )

    location = models.CharField(
        max_length=255,
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "candidates"
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["company", "email"],
                name="unique_candidate_email_per_company",
            )
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()

    class Meta:
        db_table = "candidates"
        ordering = ["-created_at"]

        constraints = [
            models.UniqueConstraint(
                fields=["company", "email"],
                name="unique_candidate_email_per_company",
            )
        ]

        indexes = [
            models.Index(fields=["company"]),
            models.Index(fields=["email"]),
            models.Index(fields=["first_name"]),
            models.Index(fields=["last_name"]),
        ]