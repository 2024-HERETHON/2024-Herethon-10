from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse_lazy
from .models import Team
from accounts.models import User
from django.shortcuts import get_object_or_404
from teams.forms import TeamModelForm, UserSearchForm
from django.core.paginator import Paginator


# 팀 생성하기
class TeamCreateView(View):
    # 모든 유저목록 가져와서 team_create.html로 렌더
    def get(self, request):
        form = TeamModelForm()
        users = User.objects.all()  # 모든 사용자를 가져옴
        return render(request, 'team_create.html', {'form': form, 'users': users})

    # 팀 생성한 후 team_list.html로 리다이렉트
    def post(self, request):
        if request.method == 'POST' or request.method == 'FILES':
            form = TeamModelForm(request.POST, request.FILES)
            if form.is_valid():
                # team = form.save()  # 폼 데이터를 DB에 저장하고 팀 객체 반환
                unfinished_team = form.save(commit=False)
                unfinished_team.creater = request.user
                unfinished_team.save()
                member_ids = request.POST.getlist('members')  # 선택된 멤버들의 ID 리스트
                
                for member_id in member_ids:
                    user = User.objects.get(pk=member_id)
                    unfinished_team.members.add(user)
                
                return redirect('teams:team_list')
        else: 
            # 폼이 유효하지 않은 경우, 다시 폼과 사용자 목록을 렌더링
            users = User.objects.all()
            form = TeamModelForm() 
        return render(request, 'team_create.html', {'form': form, 'users': users})
       
# 팀 수정하기
def team_update(request, id):
    post = get_object_or_404(Team, pk=id)
    if request.method == 'POST' or request.method == 'FILES':
        form = TeamModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('teams:team_detail')
    else:
        form = TeamModelForm(instance=post)
        return render(request, 'team_create.html', {'form':form, 'id':id})
    
# 팀 삭제하기
def team_delete(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    team.delete()
    return redirect('accounts:base') 

# 팀 전체 조회
def team_list(request):
    teams = Team.objects.all().order_by('-created_at')
    paginator = Paginator(teams, 3)
    pagnum = request.GET.get('page')
    teams = paginator.get_page(pagnum)
    return render(request, 'team_list.html', {'teams': teams})

# 팀 상세 조회
def team_detail(request, id): 
    team = get_object_or_404(Team, pk=id)
    # team = get_object_or_404(Team, pk=id)
    return render(request, 'team_detail.html', {'team' : team, 'id':id})

# 유저 찾기
# def user_search(request):
#     form = UserSearchForm(request.GET)
#     users = []

#     if form.is_valid():
#         search_query = form.cleaned_data.get('search_query')
#         if search_query:
#             users = User.objects.filter(username__icontains=search_query)

#     return render(request, 'user_search.html', {'form': form, 'users': users})