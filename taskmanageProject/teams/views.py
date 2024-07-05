from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Team, Task
from accounts.models import User
from django.shortcuts import get_object_or_404
from teams.forms import TeamModelForm, TasksModelForm, TeamUpdateModelForm
from django.core.paginator import Paginator
import json


''' 팀 '''

# 팀 생성하기
class TeamCreateView(View):
    # 모든 유저목록 가져와서 team_create.html로 렌더
    def get(self, request):
        form = TeamModelForm(current_user=request.user)
        users = User.objects.all().order_by('username')  # 모든 사용자를 가져옴
        return render(request, 'team_made.html', {'form': form, 'users': users})

    # 팀 생성한 후 team_list.html로 리다이렉트
    def post(self, request):
        if request.method == 'POST' or request.method == 'FILES':
            form = TeamModelForm(request.POST, request.FILES, current_user=request.user)
            if form.is_valid():
                # team = form.save()  # 폼 데이터를 DB에 저장하고 팀 객체 반환
                unfinished_team = form.save(commit=False)
                unfinished_team.creater = request.user
                unfinished_team.save()

                # 유저 맴버에 추가하기
                unfinished_team.members.add(request.user)

                member_ids = request.POST.getlist('members')  # 선택된 멤버들의 ID 리스트
                
                for member_id in member_ids:
                    user = User.objects.get(pk=member_id)
                    unfinished_team.members.add(user)
                
                return redirect('accounts:my_page',  id=request.user.id)
        else: 
            users = User.objects.all().order_by('username')
            form = TeamModelForm(current_user=request.user)  # 현재 로그인한 사용자 정보 전달
        return render(request, 'team_made.html', {'form': form, 'users': users})
       

# 팀 수정하기
def team_update(request, id):
    team = get_object_or_404(Team, pk=id)
    if request.method == 'POST' or request.method == 'FILES':
        form = TeamUpdateModelForm(request.POST, request.FILES, instance=team, current_user=request.user)
        if form.is_valid():
            unfinished_team = form.save(commit=False)
            unfinished_team.creater = request.user
            unfinished_team.save()

            # 유저 맴버에 추가하기
            unfinished_team.members.add(request.user)
            
            member_ids = request.POST.getlist('members')  # 선택된 멤버들의 ID 리스트
                
            for member_id in member_ids:
                user = User.objects.get(pk=member_id)
                unfinished_team.members.add(user)
            
            return redirect('teams:team_list',  id=request.user.id)
    else:
        form = TeamModelForm(instance=team, current_user=request.user)
        return render(request, 'team_member.html', {'form':form, 'id':id, 'team':team})
    

# 팀 삭제하기
def team_delete(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    team.delete()
    return redirect('accounts:base') 


# 팀 할일 조회
'''
def get_team_task_data(team):
    task_data = []
    for member in team.members.all():
        completed_tasks = Task.objects.filter(manager=member, finished=True).count()
        task_data.append({'username': member.username, 'completed_tasks': completed_tasks})
    return task_data
'''
def get_team_task_data(team_id):
    team = get_object_or_404(Team, pk=team_id)
    task_data = []
    for member in team.members.all():
        completed_tasks = Task.objects.filter(manager=member, finished=True, team=team).count()
        task_data.append({'username': member.username, 'completed_tasks': completed_tasks})
    return task_data

def get_team_task_data2(team_id):
    team = get_object_or_404(Team, pk=team_id)
    task_data = []
    for member in team.members.all():
        completed_tasks = Task.objects.filter(manager=member, finished=True, team=team).count()
        task_data.append({'username': member.username, 'completed_tasks': completed_tasks})
    team_member_count = team.members.count()
    team_task_count = Task.objects.filter(team=team).count()
    team_completed_tasks = Task.objects.filter(finished=True, team=team).count()
    return {'task_data': task_data, 'team_member_count': team_member_count, 
            'team_task_count': team_task_count, 'team_completed_tasks': team_completed_tasks}

# 팀 전체 조회
def team_list(request):
    if request.user.is_authenticated:
        liked_teams = Team.objects.filter(like_users=request.user).order_by('-created_at')
        other_teams = Team.objects.exclude(like_users=request.user).order_by('-created_at')
    else:
        liked_teams = Team.objects.none().order_by('-created_at')
        other_teams = Team.objects.all().order_by('-created_at')

    liked_team_data = {team.id: get_team_task_data(team.id) for team in liked_teams}
    other_team_data = {team.id: get_team_task_data(team.id) for team in other_teams}
    print(liked_team_data)
    context = {
        'liked_teams': liked_teams,
        'other_teams': other_teams,
        'liked_team_data': json.dumps(liked_team_data),
        'other_team_data': json.dumps(other_team_data),
    }
    return render(request, 'index.html', context)

# 팀 상세 조회
def team_detail(request, id):
    team = get_object_or_404(Team, pk=id)
    tasks = team.task_set.all()
    paginator = Paginator(tasks, 5)
    pagnum = request.GET.get('page')
    tasks = paginator.get_page(pagnum)
    
    team_data = get_team_task_data2(id)
    task_data = team_data['task_data']
    team_member_count = team_data['team_member_count']
    team_task_count = team_data['team_task_count']
    team_completed_tasks = team_data['team_completed_tasks']
    teamdata_json = json.dumps(task_data)

    return render(request, 'team_detail.html', {
        'team': team,
        'tasks': tasks,
        'task_data': task_data,
        'team_member_count': team_member_count,
        'team_task_count': team_task_count,
        'team_completed_tasks': team_completed_tasks,
        'teamdata': teamdata_json
    })







# 팀 좋아요
def likes(request, team_id):
    if request.user.is_authenticated:
        team = get_object_or_404(Team, pk=team_id)

        if team.like_users.filter(pk=request.user.pk).exists():
            team.like_users.remove(request.user)
        else:
            team.like_users.add(request.user)
        return redirect('teams:team_detail',  id=team.id)
    return redirect('teams:team_detail',  id=team.id)



''' 할 일 '''

# 할 일 생성하기
def task_create(request, id):
    team = get_object_or_404(Team, pk=id)
    if request.method == 'POST':
        form = TasksModelForm(request.POST, team=team)
        manager_ids = request.POST.getlist('manager')
        if form.is_valid():
            task_create = form.save(commit=False)
            task_create.team = team
            task_create.save()
            for manager_id in manager_ids:
                user = User.objects.get(pk=manager_id)
                task_create.manager.add(user)
            task_create.save()
            return redirect('teams:team_detail', id=id)
    else:
        form = TasksModelForm(team=team)

    tasks = Task.objects.filter(team=team)
    return render(request, 'team_todo.html', {'form': form, 'team': team, 'tasks': tasks})

# 할 일 수정하기
def task_update(request, id):
    task_update = get_object_or_404(Task, pk=id)  # 기존 할 일 객체를 가져옴
    team = task_update.team

    if request.method == 'POST':
        form = TasksModelForm(request.POST, request.FILES, instance=task_update, team=team)
        if form.is_valid():
            task_update = form.save(commit=False)
            task_update.manager.clear()
            for manager in form.cleaned_data['manager']:
                task_update.manager.add(manager)
            task_update.save()
            return redirect('teams:team_detail', id=task_update.team.id)
    else:
        form = TasksModelForm(instance=task_update, team=team)

    return render(request, 'team_todo.html', {'form': form, 'team': team, 'task_update': task_update})





# 할 일 삭제하기
def task_delete(request, id):
    task = get_object_or_404(Task, pk=id)
    team_id = task.team.id  # 할일이 속한 팀의 id를 가져옴
    task.delete()
    return redirect('teams:team_detail', id=team_id)




