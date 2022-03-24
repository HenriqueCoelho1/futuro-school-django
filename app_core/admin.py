from django.contrib import admin
from .models import CustomUser, UserStudent, UserTeacher, Course


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "name")

    # def user_type(self, obj):
    #     print()
    #     return ", ".join([m.user_type for m in print(obj.user_type.all())])


@admin.register(UserStudent)
class UserStudentAdmin(admin.ModelAdmin):
    list_display = ("user", "cpf")


@admin.register(UserTeacher)
class UserTeacherAdmin(admin.ModelAdmin):
    list_display = ("user", "register")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
