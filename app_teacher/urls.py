from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.register_teacher, name="register_teacher"),
    path("list/courses/", views.teacher_courses, name="teacher_courses"),
    path("list/students/", views.teacher_students, name="teacher_students"),
]
