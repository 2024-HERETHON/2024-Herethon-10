from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

team_router = SimpleRouter()
team_router.register('team', views.TeamViewSet) # user/ 경로에서 UserViewSet을 라우팅 

urlpatterns = [
    path('',include(team_router.urls)),
    # path('search/', views.UserListAPIView.as_view(), name='user_search_api'),
]