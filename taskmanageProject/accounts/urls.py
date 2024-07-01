from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

user_router = SimpleRouter()
user_router.register('user', views.UserViewSet) # user/ 경로에서 UserViewSet을 라우팅 

urlpatterns = [
    path('',include(user_router.urls)),
    # path('user/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('auth/', include('rest_framework.urls')),
    path('rest-auth/', include('dj_rest_auth.urls')),
]