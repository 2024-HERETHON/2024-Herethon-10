from django import forms
from accounts.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm


# 커스텀 유저
class CustomUserForm(forms.ModelForm):
    profile = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'hidden-file-input'}))
    class Meta:
        model = User
        fields = ['profile', 'username', 'password', 'email', 'name', 'phone', 'birthdate']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'userid-input',
                'placeholder': '아이디를 6자 이상 입력해주세요.',
            }),
            'email': forms.TextInput(attrs={
                'class': 'email-input',
                'placeholder': '예) rlfhvm@gmail.com',
            }),
            'password': forms.TextInput(attrs={
                'class': 'password-input',
                'placeholder': '비밀번호를 8자 이상 입력해주세요.',
            }),
            'name': forms.TextInput(attrs={
                'class': 'name-input',
                'placeholder': '예) 기로프',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'phone-input',
                'placeholder': '예) 01012345678',
            }),
            'birthdate': forms.TextInput(attrs={
                'class': 'birthdate-input',
                'placeholder': '예) 2000-01-01',
            }),
            'profile': forms.FileInput(attrs={
                'class': 'profile-input',
                'id': 'profile-input',
                'style': 'display:none;'
            }),
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # 비밀번호 해싱하기
        if commit:
            user.save()
        return user

# 커스텀 유저 업데이트    
class CustomUserUpdateForm(forms.ModelForm):
    profile = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'hidden-file-input clearable-file-input'}))
    # profile = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'hidden-file-input'}))
    class Meta:
        model = User
        fields = ['profile', 'username', 'email', 'name', 'phone', 'birthdate']
    

#--------------------------------------------------------------------------------------------------------


# class CustomPasswordChangeForm(PasswordChangeForm):
#     new_password1 = forms.CharField(
#         label='New password',
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#         min_length=8,
#         help_text="Your password can’t be too similar to your other personal information.<br>Your password must contain at least 8 characters.<br>Your password can’t be a commonly used password.<br>Your password can’t be entirely numeric."
#     )
#     new_password2 = forms.CharField(
#         label='Confirm new password',
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#         min_length=8
#     )

#     def clean_new_password1(self):
#         password1 = self.cleaned_data.get('new_password1')
#         if len(password1) < 8:
#             raise ValidationError("Password must be at least 8 characters long.")
#         return password1
    