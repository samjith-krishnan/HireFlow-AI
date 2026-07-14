from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from apps.accounts.models import User
from apps.companies.models import Company
from django.contrib.auth import authenticate


class RegisterCompanySerializer(serializers.Serializer):
  
    company_name = serializers.CharField(max_length=255)
    company_email = serializers.EmailField(required=False, allow_blank=True)
    website = serializers.URLField(required=False, allow_blank=True)
    phone_number = serializers.CharField(
        max_length=20,
        required=False,
        allow_blank=True,
    )


    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
    )
    email = serializers.EmailField()


    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "A user with this email already exists."
            )
        return value

    def validate_company_name(self, value):
        if Company.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError(
                "A company with this name already exists."
            )
        return value

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {
                    "confirm_password": "Passwords do not match."
                }
            )

        validate_password(attrs["password"])

        return attrs
    


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "role",
        )


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            "id",
            "name",
            "slug",
        )





class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            username=email,
            password=password,
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid email or password."
            )

        if not user.is_active:
            raise serializers.ValidationError(
                "Your account is inactive."
            )

        attrs["user"] = user

        return attrs