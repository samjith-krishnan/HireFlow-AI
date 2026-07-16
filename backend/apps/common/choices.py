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


class ApplicationSource(models.TextChoices):
    WEBSITE = "WEBSITE", "Website"
    LINKEDIN = "LINKEDIN", "LinkedIn"
    REFERRAL = "REFERRAL", "Referral"
    INDEED = "INDEED", "Indeed"
    OTHER = "OTHER", "Other"


class CandidateStatus(models.TextChoices):
    APPLIED = "APPLIED", "Applied"
    SHORTLISTED = "SHORTLISTED", "Shortlisted"
    INTERVIEW = "INTERVIEW", "Interview"
    OFFERED = "OFFERED", "Offered"
    HIRED = "HIRED", "Hired"
    REJECTED = "REJECTED", "Rejected"


class EmploymentType(models.TextChoices):
    FULL_TIME = "full_time", "Full Time"
    PART_TIME = "part_time", "Part Time"
    CONTRACT = "contract", "Contract"
    INTERN = "intern", "Internship"
    FREELANCE = "freelance", "Freelance"
    TEMPORARY = "temporary", "Temporary"

class JobStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    OPEN = "OPEN", "Open"
    CLOSED = "CLOSED", "Closed"
    ARCHIVED = "ARCHIVED", "Archived"


class ExperienceLevel(models.TextChoices):
    FRESHER = "FRESHER", "Fresher"
    JUNIOR = "JUNIOR", "Junior"
    MID = "MID", "Mid Level"
    SENIOR = "SENIOR", "Senior"
    LEAD = "LEAD", "Lead"