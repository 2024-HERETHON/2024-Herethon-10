# accounts/urls.py

from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.base, name='base'),
    path('signup/', views.signup, name='signup'),
    path('signup/success/', views.signup_success, name='signup_success'),
    path('signup/fail/', views.signup_fail, name='signup_fail'),
    path("user_update/<int:id>/", views.user_update, name="user_update"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),

    # 마이페이지
    path('my_page/<int:id>/', views.my_page, name='my_page'),

    #------------------------------------------------------------------------------------
    
    # 비밀번호 초기화(메일)
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),


    # path('password_reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    # path('reset/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # path('send_email/', views.send_email, name='send_email'),

    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('send_email/', auth_views.PasswordResetCompleteView.as_view(), name='send_email'),
]