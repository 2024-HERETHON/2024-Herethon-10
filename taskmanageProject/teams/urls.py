from django.urls import path, include
from . import views

app_name = "teams"

urlpatterns = [
    path('team_create/', views.TeamCreateView.as_view(), name='team_create'),
    path('team_update/<int:id>/', views.team_update, name='team_update'),
    path('team_delete/<int:team_id>/', views.team_delete, name='team_delete'),
    path('team_list/', views.team_list, name='team_list'),
    path('team_detail/<int:id>/', views.team_detail, name='team_detail'),

    # 팀 좋아요
    path('<int:team_id>/likes/', views.likes, name='likes'),
]