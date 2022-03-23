from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=200, null=False, blank=False)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "01 - User"

    def get_username(self):
        return self.email

    def __str__(self) -> str:
        return f"{self.email}"


class UserType(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.PROTECT, null=True, blank=True
    )
    identifier = models.CharField(unique=True, max_length=20, blank=False, null=False)
    USER_TYPE_CHOICES = [
        ["S", "STUDENT"],
        ["T", "TRAINER"],
    ]
    user_type = models.CharField(
        max_length=1, choices=USER_TYPE_CHOICES, blank=False, null=False, default="S"
    )

    class Meta:
        verbose_name = "02 - UserType"

    def __str__(self) -> str:
        return f"{self.email}"


# class Course(models.Model):
#     instructor = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
#     name = models.CharField(max_length=20, null=False, blank=False)
