
from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import CustomUserForm, CustomUserUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from teams.models import Team


# 첫 화면
def base(request):
    return render(request, 'account_base.html')

# 회원가입
def signup(request):
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
                    # 장고 관리 페이지에 뜬다.
                    messages.error(request, "아이디는 6~25자여야 합니다.")
                    return redirect('accounts:signup_fail')
                
            # 2. 비밀번호 길이 검사
                if len(password) < 8:
                    messages.error(request, "비밀번호는 최소 8자 이상이어야 합니다.")
                    return redirect('accounts:signup_fail')
                
            # 3. 이름 길이 검사
                if len(name) < 2 or len(name) > 15:
                    messages.error(request, "이름은 2~10자이어야 합니다.")
                    return redirect('accounts:signup_fail')
                
            # 4. 전화번호 중복 & 길이 검사
                if User.objects.filter(phone=phone).exists():
                    messages.error(request, "이미 가입되어있는 전화번호입니다.")
                    return redirect('accounts:signup_fail')
                
                if len(phone) != 11:
                    messages.error(request, "전화번호는 '-'를 제외한 11자리로 작성해주세요.")
                    return redirect('accounts:signup_fail')
                
            # 5. 이메일 중복 검사
                if User.objects.filter(email=email).exists():
                    messages.error(request, "이미 가입되어있는 이메일 주소입니다.")
                    return redirect('accounts:signup_fail')
                
                # 회원가입 성공
                form.save()
                return redirect('accounts:base') 
            else:
                return redirect('accounts:signup_fail') # 비번 불일치
        else:
            return redirect('accounts:signup_fail') # 아이디 중복 or 이메일 @ 미포함시
    else:
        form = CustomUserForm()

    return render(request, 'signup.html', {'form': form})

# 회원가입 성공
def signup_success(request):
    return render(request, 'account_base.html')

# 회원가입 실패
def signup_fail(request):
    return render(request, 'signup_fail.html')

# 회원정보 수정
def user_update(request, id):
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
                # 장고 관리 페이지에 뜬다.
                messages.error(request, "아이디는 6~25자여야 합니다.")
                return redirect('accounts:signup_fail')
            
        # 2. 이름 길이 검사
            if len(name) < 2 or len(name) > 15:
                messages.error(request, "이름은 2~10자이어야 합니다.")
                return redirect('accounts:signup_fail')
            
        # 3. 전화번호 중복 & 길이 검사
            if User.objects.filter(phone=phone).exclude(pk=user.pk).exists():
                messages.error(request, "이미 가입되어있는 전화번호입니다.")
                return redirect('accounts:signup_fail')
            
            if len(phone) != 11:
                messages.error(request, "전화번호는 '-'를 제외한 11자리로 작성해주세요.")
                return redirect('accounts:signup_fail')
            
        # 4. 이메일 중복 검사
            if User.objects.filter(email=email).exclude(pk=user.pk).exists():
                messages.error(request, "이미 가입되어있는 이메일 주소입니다.")
                return redirect('accounts:signup_fail')

            user.username = username
            user.name = name
            user.phone = phone
            user.email = email
            user.birthdate = birthdate

            # 회원 수정 성공
            form.save()
            return redirect('accounts:base') 
        else:
            return redirect('accounts:signup_fail') # 아이디 중복 or 이메일 @ 미포함시
    else:
        form = CustomUserUpdateForm(instance=user)

    return render(request, 'signup.html', {'form':form, 'id':id})
    
# 로그인
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print('로그인 성공')
            return redirect('accounts:base')
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
    return redirect('accounts:base') 

# 마이페이지
def my_page(request, id):
    user = get_object_or_404(User, pk=id)
    teams = Team.objects.filter(creater=user)
    return render(request, 'my_page.html', {'user': user, 'teams':teams, 'id':id})


#-------------------------------------------------------------------------------------------------

    
# 메일 보내기(참고용)
from django.core.mail.message import EmailMessage

def send_email(request):
    subject = "message"
    to = ["hayoun1114@naver.com"]
    from_email = "taskmanager202407@naver.com"
    message = "메지시 테스트"
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()