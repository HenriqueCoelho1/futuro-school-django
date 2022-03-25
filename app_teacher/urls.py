from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.RegisterTeacher.as_view(), name="register_teacher"),
    path("new/course", views.RegisterCourse.as_view(), name="register_course"),
    path(
        "register/course/",
        views.RegisterTeacherCourse.as_view(),
        name="register_teacher_course",
    ),
    path("list/courses/", views.TeacherCourses.as_view(), name="teacher_courses"),
    path(
        "list/course/<int:id>", views.CourseStudents.as_view(), name="course_students"
    ),
]
