from django import forms
from accounts.models import User
from django.core.exceptions import ValidationError

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name', 'phone', 'birthdate']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # 비밀번호 해싱하기
        if commit:
            user.save()
        return user
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("이미 사용중인 아이디입니다.")
        return username