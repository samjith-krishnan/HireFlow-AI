from django.db import models
from django.utils.text import slugify

from apps.common.models import BaseModel
from apps.common.choices import (
    EmploymentType,
    JobStatus,
)


class Job(BaseModel):

    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="jobs",
    )

    department = models.ForeignKey(
        "companies.Department",
        on_delete=models.SET_NULL,
        related_name="jobs",
        null=True,
        blank=True,
    )

    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        related_name="created_jobs",
        null=True,
    )

    title = models.CharField(
        max_length=255,
    )

    slug = models.SlugField(
        max_length=255,
        blank=True,
    )

    description = models.TextField()

    responsibilities = models.TextField(
        blank=True,
    )

    requirements = models.TextField(
        blank=True,
    )

    location = models.CharField(
        max_length=255,
        blank=True,
    )

    employment_type = models.CharField(
        max_length=20,
        choices=EmploymentType.choices,
        default=EmploymentType.FULL_TIME,
    )

    minimum_experience = models.PositiveIntegerField(
        default=0,
        help_text="Years",
    )

    maximum_experience = models.PositiveIntegerField(
        default=0,
        help_text="Years",
    )

    minimum_salary = models.PositiveIntegerField(
        default=0,
    )

    maximum_salary = models.PositiveIntegerField(
        default=0,
    )

    vacancies = models.PositiveIntegerField(
        default=1,
    )

    deadline = models.DateField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=JobStatus.choices,
        default=JobStatus.DRAFT,
    )

    skills = models.ManyToManyField(
        "skills.Skill",
        related_name="jobs",
        blank=True,
    )

    is_remote = models.BooleanField(
        default=False,
    )

    is_featured = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "jobs"
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["company", "slug"],
                name="unique_job_slug_per_company",
            )
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title