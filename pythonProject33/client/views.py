from rest_framework import generics

from client.serializers import UserSerializer


class UserRegister(generics.CreateAPIView):
    serializer_class = UserSerializer
