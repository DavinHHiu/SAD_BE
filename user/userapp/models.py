from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import status
import re


class FullName(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)


class Address(models.Model):
    street = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)


class Account(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)


class User(models.Model):
    email = models.EmailField(unique=True)
    fullname = models.ForeignKey(FullName, on_delete=models.SET_NULL, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def is_valid(self, *args, **kwargs):
        if not self.is_valid_email():
            return {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Email không hợp lệ",
            }
        if self.email.strip() and kwargs and not kwargs["is_update"]:
            userDB = User.objects.filter(email=self.email).first()
            if userDB:
                return {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Email đã tồn tại",
                }

        if (
            self.account
            and self.account.username.strip()
            and kwargs
            and not kwargs["is_update"]
        ):
            accountDB = Account.objects.filter(username=self.account.username).first()
            if accountDB:
                return {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Tên người dùng đã tồn tại",
                }

        return {
            "status": status.HTTP_201_CREATED,
            "message": "Đăng ký thành công",
        }

    def is_valid_email(self):
        if not self.email.strip():
            return False
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        return bool(re.match(pattern, self.email))
