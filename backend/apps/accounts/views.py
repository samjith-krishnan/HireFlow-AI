from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterCompanySerializer
from .services import AuthService


class RegisterCompanyAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterCompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = AuthService.register_company(
            serializer.validated_data
        )

        return Response(
            {
                "success": True,
                "message": "Company registered successfully.",
                "data": data,
            },
            status=status.HTTP_201_CREATED,
        )