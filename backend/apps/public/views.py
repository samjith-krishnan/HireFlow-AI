from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.jobs.selectors import JobSelector

from .serializers import PublicJobSerializer


class PublicJobAPIView(RetrieveAPIView):
    serializer_class = PublicJobSerializer
    permission_classes = [AllowAny]

    lookup_url_kwarg = "apply_token"

    def get_object(self):
        return JobSelector.get_public_job(
            apply_token=self.kwargs["apply_token"],
        )