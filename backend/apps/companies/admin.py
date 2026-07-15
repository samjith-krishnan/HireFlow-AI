from django.contrib import admin

from .models import Company, Department


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "is_active",
    )
    search_fields = (
        "name",
        "email",
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "company",
        "is_active",
    )
    list_filter = (
        "company",
        "is_active",
    )
    search_fields = (
        "name",
    )