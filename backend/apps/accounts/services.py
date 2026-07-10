from django.db import transaction
from rest_framework_simplejwt.tokens import RefreshToken

from apps.accounts.models import User
from apps.common.choices import UserRole
from apps.companies.models import Company
from apps.accounts.serializers import (
    UserSerializer,
    CompanySerializer,
)

class AuthService:

    @staticmethod
    @transaction.atomic
    def register_company(validated_data):

        company = Company.objects.create(
            name=validated_data["company_name"],
            email=validated_data.get("company_email", ""),
            phone_number=validated_data.get("phone_number", ""),
            website=validated_data.get("website", ""),
        )

        owner = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data.get("last_name", ""),
            company=company,
            role=UserRole.OWNER,
            is_active=True,
            is_verified=True,
        )

        refresh = RefreshToken.for_user(owner)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": UserSerializer(owner).data,
            "company": CompanySerializer(company).data,
        }