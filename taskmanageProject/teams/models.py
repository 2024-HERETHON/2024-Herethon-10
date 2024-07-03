from django.db import models
from accounts.models import User

class Team(models.Model):
    name = models.CharField(verbose_name="팀 이름", max_length=100)
    description = models.TextField(verbose_name="팀 설명", blank=True)
    members = models.ManyToManyField(User, related_name='teams', blank=True)
    created_at = models.DateTimeField(verbose_name="팀 생성일", auto_now_add=True)
    creater = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(verbose_name="팀이미지", blank=True, null=True, upload_to='team_photo', default='team_photo/default_photo.jpg')
    like_users = models.ManyToManyField(User, related_name='like_teams')

    def __str__(self):
        return self.name
    
    def like_count(self):
        return self.like_users.count()
