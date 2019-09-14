from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserListView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = UserSerializer
    queryset = User.objects.all()
