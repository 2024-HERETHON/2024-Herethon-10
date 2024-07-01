from .models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    def validate(self, data):
            # 비밀번호와 비밀번호 확인이 일치하는지 확인합니다.
            if data.get('password') != data.get('password_confirm'):
                raise serializers.ValidationError("Passwords do not match.")
            return data
    
    def validate_email(self, data):
        if User.objects.filter(email=data).exists():
            raise serializers.ValidationError("This email is already in use.")
        return data
    
    def create(self, validated_data): 
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        # user = User.objects.create_user(
        #     username = validated_data['username'], 
        #     email = validated_data['email'],
        #     name = validated_data['name'],
        #     password = validated_data['password'], 
        #     birthdate = validated_data['birthdate'],
        #     phone = validated_data['phone']
        # )
        return user 
    class Meta: 
        model = User
        fields = ['username', 'email', 'name', 'password', 'password_confirm', 'birthdate', 'phone' ] 