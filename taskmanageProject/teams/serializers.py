from rest_framework import serializers
from .models import Team
from accounts.models import User

# 사용자 모델 직렬화
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'phone', 'birthdate')
    
# 팀 모델 직렬화
class TeamSerializer(serializers.ModelSerializer):
    # 다대다, 읽기 전용(쓰기x)
    # members = UserSerializer(many=True, read_only=True) 

    members = serializers.SlugRelatedField(
            queryset=User.objects.all(),
            slug_field='username',
            many=True
    )
    
    class Meta:
        model = Team
        fields = ('id', 'name', 'description', 'members')

    # 입력 시에는 사용자 'username' 목록 받고, 출력 시에는 사용자 정보 반환
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['members'] = UserSerializer(instance.members, many=True).data
        return representation
