from django.urls import path, include


urlpatterns = [
    path("user/", include("app_student.urls")),
    path("teacher/", include("app_teacher.urls")),
]
