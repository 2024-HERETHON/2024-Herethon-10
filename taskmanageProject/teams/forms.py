from django import forms
from .models import Team
from accounts.models import User

class TeamModelForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'description', 'members', 'photo']
        widgets = {
            'members': forms.CheckboxSelectMultiple(),  # 여러 명 선택 가능한 체크박스 위젯
        }

    # members 필드에 있는 queryset을 이름 순서로 정렬
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['members'].queryset = User.objects.all().order_by('username')

# 유저 찾기(자바스크립트로 구현해야함)
class UserSearchForm(forms.Form):
    search_query = forms.CharField(label='Search users', max_length=100)