from django.urls import path, include


urlpatterns = [
    path("user/", include("app_student.urls")),
    # path("instructor/", include("app_instructor.urls")),
]
