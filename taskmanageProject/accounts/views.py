
from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import CustomUserForm, CustomUserUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash
from teams.models import Team
from django.views.decorators.csrf import csrf_exempt

# 첫 화면
def base(request):
    return render(request, 'account_base.html')

# 회원가입
@csrf_exempt
def signup(request,  edit=False):
    if request.method == 'POST' or request.method == 'FILES':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            if request.POST['password'] == request.POST['repeat']:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                email = form.cleaned_data['email']
                birthdate = form.cleaned_data['birthdate']

            # 1. 아이디 길이 검사
                if len(username) < 6 or len(username) > 25:
                    error_message = "아이디를 6자 이상 입력해주세요." 
                    return render(request, 'join.html', {'error_message': error_message, 'form': form, 'is_edit': edit})
                
            # 2. 비밀번호 길이 검사
                if len(password) < 8:
                    error_message = "비밀번호를 8자 이상 입력해주세요." 
                    return render(request, 'join.html', {'error_message': error_message, 'form': form, 'is_edit': edit})
                
            # 3. 이름 길이 검사
                if len(name) < 2 or len(name) > 15:
                    error_message = "이름을 2자 이상 입력해주세요." 
                    return render(request, 'join.html', {'error_message': error_message, 'form': form, 'is_edit': edit})
                
            # 4. 전화번호 중복 & 길이 검사
                if User.objects.filter(phone=phone).exists():
                    error_message = "이미 가입되어있는 전화번호입니다." 
                    return render(request, 'join.html', {'error_message': error_message, 'form': form, 'is_edit': edit})
                
                if len(phone) != 11:
                    error_message = "'-'를 제외한 전화번호를 입력해주세요." 
                    return render(request, 'join.html', {'error_message': error_message, 'form': form, 'is_edit': edit})
                
            # 5. 이메일 중복 검사
                if User.objects.filter(email=email).exists():
                    error_message = "이미 존재하는 이메일입니다." 
                    return render(request, 'join.html', {'error_message': error_message, 'form': form, 'is_edit': edit})
                
                # 회원가입 성공
                form.save()
                return redirect('teams:team_list') 
            
            # 6. 비밀번호 일치 안할 경우
            else: 
                error_message = "비밀번호가 일치하지 않습니다." 
                return render(request, 'join.html', {'error_message': error_message, 'form': form, 'is_edit': edit})
        # 7. 아이디가 이미 존재할 경우
        else:
            error_message = "이미 존재하는 아이디입니다." 
            return render(request, 'join.html', {'error_message': error_message, 'form': form, 'is_edit': edit})
    else:
        form = CustomUserForm()

    return render(request, 'join.html', {'form': form, 'is_edit': edit})



# 회원정보 수정
def user_update(request, id, edit=True):
    user = get_object_or_404(User, pk=id)

    if request.method == 'POST' or request.method == 'FILES':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            birthdate = form.cleaned_data['birthdate']

        # 1. 아이디 길이 검사
            if len(username) < 6 or len(username) > 25:
                error_message = "아이디를 6자 이상 입력해주세요." 
                return render(request, 'signup.html', {'error_message': error_message, 'form': form, 'is_edit': edit})
            
        # 2. 이름 길이 검사
            if len(name) < 2 or len(name) > 15:
                error_message = "이름을 2자 이상 입력해주세요." 
                return render(request, 'signup.html', {'error_message': error_message, 'form': form, 'is_edit': edit})
            
         # 3. 전화번호 중복 & 길이 검사
            if User.objects.filter(phone=phone).exclude(pk=user.pk).exists():
                error_message = "이미 가입되어있는 전화번호입니다." 
                return render(request, 'signup.html', {'error_message': error_message, 'form': form, 'is_edit': edit})
            
            if len(phone) != 11:
                error_message = "'-'를 제외한 전화번호를 입력해주세요." 
                return render(request, 'signup.html', {'error_message': error_message, 'form': form, 'is_edit': edit})
            
        # 4. 이메일 중복 검사
            if User.objects.filter(email=email).exclude(pk=user.pk).exists():
                error_message = "이미 존재하는 이메일입니다." 
                return render(request, 'signup.html', {'error_message': error_message, 'form': form, 'is_edit': edit})

            user.username = username
            user.name = name
            user.phone = phone
            user.email = email
            user.birthdate = birthdate

            # 회원 수정 성공
            form.save()
            return redirect('teams:team_list') 
        
        #  5. 아이디가 이미 존재할 경우
        else:
            error_message = "이미 존재하는 아이디입니다." 
            return render(request, 'signup.html', {'error_message': error_message, 'form': form, 'is_edit': edit})
    else:
        form = CustomUserUpdateForm(instance=user)

    return render(request, 'signup.html', {'form':form, 'id':id, 'is_edit': edit})



# 로그인
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print('로그인 성공')
            return redirect('teams:team_list')
        else: 
            # 에러 메시지 설정
            error_message = "아이디 또는 비밀번호가 잘못되었습니다." 
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    

# 로그아웃
def logout(request):
    auth_logout(request)
    print('로그아웃 성공')
    return redirect('teams:team_list') 


# 마이페이지
def my_page(request, id):
    user = get_object_or_404(User, pk=id)
    teams = Team.objects.filter(creater=user)
    return render(request, 'mypage.html', {'user': user, 'teams':teams, 'id':id})


#-------------------------------------------------------------------------------------------------

    
# 메일 보내기(참고용)
from django.core.mail.message import EmailMessage

def send_email(request):
    subject = "message"
    to = ["hayoun1114@naver.com"]
    from_email = "taskmanager202407@naver.com"
    message = "메지시 테스트"
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()