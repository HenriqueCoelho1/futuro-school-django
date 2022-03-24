from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class CustomUser(AbstractUser):
    name = models.CharField(max_length=200, null=False, blank=False)
    username = models.CharField(unique=True, max_length=200, null=False, blank=False)
    email = models.EmailField(unique=True, max_length=200, null=False, blank=False)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "01 - User"

    def get_username(self):
        return self.email

    def __str__(self) -> str:
        return f"{self.email}"


class UserTeacher(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="teacher"
    )
    register = models.CharField(max_length=20, null=False, blank=False)


class Course(models.Model):
    name = models.CharField(max_length=20)
    teacher = models.ForeignKey(
        UserTeacher, on_delete=models.CASCADE, null=True, blank=True
    )


class UserStudent(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="student"
    )
    cpf = models.CharField(max_length=16, unique=True, blank=True, null=True)
    courses = models.ManyToManyField(Course, related_name="students")
