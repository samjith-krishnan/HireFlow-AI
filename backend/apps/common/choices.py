from django.db import models


class UserRole(models.TextChoices):
    OWNER = "OWNER", "Owner"
    ADMIN = "ADMIN", "Admin"
    HR = "HR", "HR"
    RECRUITER = "RECRUITER", "Recruiter"
    INTERVIEWER = "INTERVIEWER", "Interviewer"

class CompanySize(models.TextChoices):
    SOLO = "SOLO", "1"
    SMALL = "SMALL", "2-10"
    MEDIUM = "MEDIUM", "11-50"
    LARGE = "LARGE", "51-200"
    ENTERPRISE = "ENTERPRISE", "200+"