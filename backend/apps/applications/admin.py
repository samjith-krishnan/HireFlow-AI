from django.contrib import admin

from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "candidate",
        "job",
        "status",
        "ai_score",
        "source",
        "created_at",
    )

    list_filter = (
        "status",
        "source",
        "created_at",
    )

    search_fields = (
        "candidate__first_name",
        "candidate__last_name",
        "candidate__email",
        "job__title",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
        "resume_text",
        "parsed_data",
        "ai_score",
    )