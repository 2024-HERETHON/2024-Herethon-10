"""
URL configuration for taskmanageProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('accounts.urls', namespace='accounts')),
    path('team/',include('teams.urls', namespace='teams')),

    # 비밀번호 재설정(메일 전송)
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='../../accounts/templates/registration/find_password.html',  # 커스터마이즈한 템플릿 경로 지정
        email_template_name='../../accounts/templates/registration/password_reset_email.html',  # 이메일 템플릿 경로 지정
        subject_template_name='../../accounts/templates/registration/password_reset_subject.txt'  # 이메일 제목 템플릿 경로 지정
    ), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='../../accounts/templates/registration/find_passwordOK.html' 
    ), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='../../accounts/templates/registration/modify_password.html' 
    ), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='../../accounts/templates/registration/modify_OK.html' 
    ), name="password_reset_complete"),
]

# 이미지 루트
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)