from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.RegisterStudent.as_view(), name="register_student"),
    path("list/", views.StudentCourses.as_view(), name="student_courses"),
]
