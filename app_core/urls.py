from django.urls import path, include
from .views import GetOut, Access, Index


urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("login/", Access.as_view(), name="access"),
    path("getout", GetOut.as_view(), name="getout"),
    path("student/", include("app_student.urls")),
    path("teacher/", include("app_teacher.urls")),
]
