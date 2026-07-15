from django.urls import path

from .views import (
    SkillListCreateAPIView,
    SkillRetrieveUpdateDestroyAPIView,
)

app_name = "skills"

urlpatterns = [
    path("",SkillListCreateAPIView.as_view(),name="skill-list-create" ),
    path( "<uuid:id>/",SkillRetrieveUpdateDestroyAPIView.as_view(), name="skill-detail",),
]