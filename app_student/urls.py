from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.register_student, name="register_student"),
    path("list/", views.student_courses, name="student_courses"),
]
