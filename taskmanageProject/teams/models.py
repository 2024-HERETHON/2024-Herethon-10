from django.db import models
from accounts.models import User

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100) # 팀 이름
    description = models.TextField(blank=True) # 팀 설명
    members = models.ManyToManyField(User, related_name='teams', blank=True)
    # 다대다 관계
    # 한 팀에 여러 사용자 속할 수 O
    # 각 사용자가 여러 팀에 속할 수 O

    def __str__(self):
        return self.name # 팀 이름 반환
