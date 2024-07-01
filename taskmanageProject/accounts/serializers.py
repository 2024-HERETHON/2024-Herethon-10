import re
from .models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    username = serializers.CharField(min_length=6, 
                                     max_length=25,
                                     help_text='6~25자 입력가능.', 
                                     required=True)
    name = serializers.CharField(min_length=2, 
                                 max_length=10,
                                 help_text='2~10자 입력가능.')
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, 
                                     min_length=8,
                                     help_text='8자이상 입력해주세요.')
    password_confirm = serializers.CharField(write_only=True, min_length=8)
    phone = serializers.CharField(max_length=13, validators=[],)
        
    # username 중복 확인
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('이미 사용 중인 username입니다.')
        return value
    
    # 비밀번호 일치 확인
    def validate(self, data):
            # 비밀번호와 비밀번호 확인이 일치하는지 확인합니다.
            if data.get('password') != data.get('password_confirm'):
                raise serializers.ValidationError("Passwords do not match.")
            return data
    
    # 이메일 중복 확인
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value
    
    # 전화번호 입력 형태
    def validate_phone(self, value):
        # 전화번호에서 '-'를 제거
        phone = value.replace('-', '')
        # 숫자만 포함되어 있는지 검사
        if not phone.isdigit():
            raise serializers.ValidationError("전화번호는 숫자와 '-'만 포함해야 합니다.")
        # 11자리인지 검사
        if len(phone) != 11 and len(phone) != 13:
            raise serializers.ValidationError("전화번호 형식이 잘못되었습니다. 11자 혹은 하이픈 포함 13자로 작성해주세요.")
        if User.objects.filter(phone=value).exists():
            raise serializers.ValidationError("This phone is already in use.")
        # 010-0000-0000 형식으로 변환
        return f'{phone[:3]}-{phone[3:7]}-{phone[7:]}'
    
    # 유저 생성
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