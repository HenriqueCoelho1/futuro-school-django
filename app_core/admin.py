from django.contrib import admin
from .models import CustomUser, UserStudent, UserTeacher, Course


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "name")


@admin.register(UserStudent)
class UserStudentAdmin(admin.ModelAdmin):
    list_display = ("user", "cpf")


@admin.register(UserTeacher)
class UserTeacherAdmin(admin.ModelAdmin):
    list_display = ("user", "register")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
