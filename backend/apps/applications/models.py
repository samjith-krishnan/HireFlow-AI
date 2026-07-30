from django.db import models

from apps.common.models import BaseModel
from apps.common.choices import (
    ApplicationStatus,
    ApplicationSource,
)


class Application(BaseModel):
    candidate = models.ForeignKey(
        "candidates.Candidate",
        on_delete=models.CASCADE,
        related_name="applications",
    )

    job = models.ForeignKey(
        "jobs.Job",
        on_delete=models.CASCADE,
        related_name="applications",
    )

    resume = models.FileField(
        upload_to="applications/resumes/",
    )

    cover_letter = models.TextField(
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.APPLIED,
    )

    source = models.CharField(
        max_length=20,
        choices=ApplicationSource.choices,
        default=ApplicationSource.CAREER_PORTAL,
    )

    ai_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )

    resume_text = models.TextField(
        blank=True,
    )

    parsed_data = models.JSONField(
        default=dict,
        blank=True,
    )

    reviewed_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_applications",
    )

    reviewed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    notes = models.TextField(
        blank=True,
    )

    class Meta:
        db_table = "applications"
        ordering = ["-created_at"]

        constraints = [
            models.UniqueConstraint(
                fields=["candidate", "job"],
                name="unique_candidate_job_application",
            )
        ]

        indexes = [
            models.Index(fields=["job"]),
            models.Index(fields=["candidate"]),
            models.Index(fields=["status"]),
            models.Index(fields=["ai_score"]),
        ]

    def __str__(self):
        return f"{self.candidate.first_name} - {self.job.title}"