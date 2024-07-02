from django import forms
from accounts.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile', 'username', 'password', 'email', 'name', 'phone', 'birthdate']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # 비밀번호 해싱하기
        if commit:
            user.save()
        return user
    
class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile', 'username', 'email', 'name', 'phone', 'birthdate']
    

#--------------------------------------------------------------------------------------------------------



class CustomPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8,
        help_text="Your password can’t be too similar to your other personal information.<br>Your password must contain at least 8 characters.<br>Your password can’t be a commonly used password.<br>Your password can’t be entirely numeric."
    )
    new_password2 = forms.CharField(
        label='Confirm new password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8
    )

    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return password1
    