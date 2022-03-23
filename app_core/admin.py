from django.contrib import admin
from .models import CustomUser, UserType


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name")

    # def user_type(self, obj):
    #     print()
    #     return ", ".join([m.user_type for m in print(obj.user_type.all())])


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ("identifier", "user")