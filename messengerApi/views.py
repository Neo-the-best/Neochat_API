from .models import User
from .serializers import UserSerializer, ProfileSerializer
from .pagination import UserPagination
from rest_framework import generics
from django.http import HttpResponse, JsonResponse


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination


class ProfileList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer