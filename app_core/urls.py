from django.urls import path, include
from .views import access, getout, index


urlpatterns = [
    path("", index, name="index"),
    path("login/", access, name="access"),
    path("getout", getout, name="getout"),
    path("student/", include("app_student.urls")),
    path("teacher/", include("app_teacher.urls")),
]
