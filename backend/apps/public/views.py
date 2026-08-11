from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.jobs.selectors import JobSelector

from .serializers import PublicJobSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


from apps.applications.services import ApplicationService

from .serializers import (
    PublicJobSerializer,
    PublicApplySerializer,
)




class PublicJobAPIView(RetrieveAPIView):
    serializer_class = PublicJobSerializer
    permission_classes = [AllowAny]

    lookup_url_kwarg = "apply_token"

    def get_object(self):
        return JobSelector.get_public_job(
            apply_token=self.kwargs["apply_token"],
        )




class PublicJobAPIView(RetrieveAPIView):
    serializer_class = PublicJobSerializer
    permission_classes = [AllowAny]

    lookup_url_kwarg = "apply_token"

    def get_object(self):
        return JobSelector.get_public_job(
            apply_token=self.kwargs["apply_token"],
        )


class PublicApplyAPIView(GenericAPIView):
    serializer_class = PublicApplySerializer
    permission_classes = [AllowAny]

    def post(self, request, apply_token):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        job = JobSelector.get_public_job(apply_token)

        application = ApplicationService.create_application(
            job=job,
            first_name=serializer.validated_data["first_name"],
            last_name=serializer.validated_data["last_name"],
            email=serializer.validated_data["email"],
            phone_number=serializer.validated_data["phone_number"],
            resume=serializer.validated_data["resume"],
            cover_letter=serializer.validated_data["cover_letter"],
        )

        return Response(
            {
                "message": "Application submitted successfully.",
                "application_id": application.id,
            },
            status=status.HTTP_201_CREATED,
        )