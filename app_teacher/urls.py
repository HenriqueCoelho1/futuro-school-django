from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.register_teacher, name="register_teacher"),
    path("new/course", views.register_course, name="register_course"),
    path(
        "register/course",
        views.register_teacher_course,
        name="register_teacher_course",
    ),
    path("list/courses/", views.teacher_courses, name="teacher_courses"),
    path("list/course/<int:id>", views.course_students, name="course_students"),
]
