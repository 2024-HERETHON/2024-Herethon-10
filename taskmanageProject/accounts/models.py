from django.db import models
from django.contrib.auth.models import AbstractUser # AbstractUser 불러오기

# Create your models here.
class User(AbstractUser):
    username = models.CharField(verbose_name='아이디', null=False, blank=False, unique=True, max_length=25)
    name = models.CharField(verbose_name='이름', max_length=30)
    email = models.EmailField(unique=True)
    birthdate = models.DateField(verbose_name='생년월일', blank=True, null=True)
    phone = models.CharField(verbose_name='전화번호', max_length=30, unique=True)
   
    def __str__(self):
        return self.username