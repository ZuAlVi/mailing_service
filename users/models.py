from django.contrib.auth.models import AbstractUser
from django.db import models

from mailings.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=30, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    code = models.CharField(max_length=12, verbose_name='код', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
