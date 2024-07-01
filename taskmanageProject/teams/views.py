from django.shortcuts import render
from .models import Team
from .serializers import TeamSerializer
from accounts.serializers import UserSerializer
from rest_framework import viewsets, generics, filters
from accounts.models import User

# Create your views here.
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

# 검색 API
# class UserListAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['username'] 
# UserListAPIView를 사용하여 API 엔드포인트를 만들면, 
# 클라이언트에서 GET 요청을 통해 ?search= 쿼리를 추가하여 
# username을 기준으로 검색할 수 있다.
# 예를 들어, /team/?search=johndoe와 같은 요청을 보내면 
# username이 "johndoe"인 모든 사용자를 검색할 수 있습니다.
