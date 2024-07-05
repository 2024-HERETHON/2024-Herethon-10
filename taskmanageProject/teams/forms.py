from django import forms
from .models import Team, Task
from accounts.models import User


# Team 모델폼
class TeamModelForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'title_input',
            'placeholder': 'Untitled',
            })
    )
    # name = forms.CharField(widget=forms.ClearableFileInput(attrs={'class': '.title_input'}))
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'hidden-file-input'}))
    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user', None)
        super().__init__(*args, **kwargs)
        
        # 유저 제외하고 체크박스 생성
        if current_user:
            users = User.objects.filter(is_superuser=False).exclude(pk=current_user.pk).order_by('username')
        else:
            users = User.objects.filter(is_superuser=False).order_by('username')
        
        self.fields['members'].queryset = users

    class Meta:
        model = Team
        fields = ['name', 'description', 'members', 'photo']
        ordering = ['-created_at']
        widgets = {
            'members': forms.CheckboxSelectMultiple(),  # 여러 명 선택 가능한 체크박스 위젯
        }
       
class TeamUpdateModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user', None)
        super().__init__(*args, **kwargs)
        
        # 유저 제외하고 체크박스 생성
        if current_user:
            users = User.objects.filter(is_superuser=False).exclude(pk=current_user.pk).order_by('username')
        else:
            users = User.objects.filter(is_superuser=False).order_by('username')
        
        self.fields['members'].queryset = users

    class Meta:
        model = Team
        fields = ['members']
        widgets = {
            'members': forms.CheckboxSelectMultiple(),  # 여러 명 선택 가능한 체크박스 위젯
        }


# Task 모델폼
class TasksModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        team = kwargs.pop('team', None)
        super(TasksModelForm, self).__init__(*args, **kwargs)
        if team:
            self.fields['manager'].queryset = team.members.all()

    # def clean(self):
    #     cleaned_data = super().clean()
    #     manager_ids = self.cleaned_data.get('manager')
    #     if manager_ids:
    #         cleaned_data['manager'] = User.objects.filter(pk__in=manager_ids)
    #     return cleaned_data
    
    def clean(self):
        cleaned_data = super().clean()
        manager_ids = cleaned_data.get('manager')
        if not manager_ids:
            self.add_error('manager', '담당자를 선택해주세요.')
        return cleaned_data

    class Meta:
        model = Task
        fields = ['title', 'manager', 'finished']
        widgets = {
            'manager': forms.CheckboxSelectMultiple()
        }
