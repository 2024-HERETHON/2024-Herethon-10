from django.db import models
from django.contrib.auth.models import AbstractUser # AbstractUser 불러오기

# 유저 커스텀
class User(AbstractUser):
    profile = models.ImageField(verbose_name='프로필', blank=True, null=True, upload_to='profile_photo', default='profile_photo/default_profile.jpg')
    username = models.CharField(verbose_name='아이디', null=False, blank=False, unique=True, max_length=40)
    name = models.CharField(verbose_name='이름', max_length=40)
    email = models.EmailField()
    birthdate = models.DateField(verbose_name='생년월일', blank=True, null=True)
    phone = models.CharField(verbose_name='전화번호', max_length=40)
        
    def __str__(self):
        return self.username
    