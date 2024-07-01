
from django.shortcuts import render, redirect
from .models import User
from .forms import CustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

# 회원가입
def signup(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            if request.POST['password'] == request.POST['repeat']:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                email = form.cleaned_data['email']

            # 1. 아이디 유효성 검사
                if len(username) < 6 or len(username) > 25:
                    # 장고 관리 페이지에 뜬다.
                    messages.error(request, "아이디는 6~25자여야 합니다.")
                    return redirect('signup')
                
                if User.objects.filter(username=username).exists():
                    messages.error(request, "이미 사용중인 아이디입니다.")
                    return redirect('signup')
                
            # 2. 비밀번호 유효성 검사
                if len(password) < 8:
                    messages.error(request, "비밀번호는 최소 8자 이상이어야 합니다.")
                    return redirect('signup')
                
            # 3. 이름 유효성 검사
                if len(name) < 2 or len(name) > 10:
                    messages.error(request, "이름은 2~10자이어야 합니다.")
                    return redirect('signup')
                
            # 4. 전화번호 유효성 검사
                if User.objects.filter(phone=phone).exists():
                    messages.error(request, "이미 가입되어있는 전화번호입니다.")
                    return redirect('signup')
                
                if len(phone) != 11 and len(phone) != 13:
                    messages.error(request, "전화번호는 10자리 혹은 13자리(하이픈 포함)이어야 합니다.")
                    return redirect('signup')
                
            # 5. 이메일 유효성 검사
                if '@' not in email:
                    messages.error(request, "올바른 이메일 형식이 아닙니다.")
                    return redirect('signup')
                
                if User.objects.filter(email=email).exists():
                    messages.error(request, "이미 가입되어있는 이메일 주소입니다.")
                    # form.add_error('email', '이미 등록된 이메일 주소입니다.')  # 폼에 오류 추가
                    return redirect('signup')
                
                form.save()
                print('회원가입 성공')
                return redirect('accounts:signup_success') # 임시 템플릿 설정
    else:
        form = CustomUserForm()

    return render(request, 'signup.html', {'form': form})

# 회원가입 성공
def signup_success(request):
    # print('회원가입 성공')
    return render(request, 'signup_success.html')

# 로그인
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print('로그인 성공')
            return redirect('accounts:signup_success')
        else: 
            # 에러 메시지 설정
            error_message = "아이디 또는 비밀번호가 잘못되었습니다." 
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    
# 로그아웃
def logout(request):
    return redirect('accounts:signup') # 임시 템플릿 설정