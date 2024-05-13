from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.serializers import UserSerializer

UserModel = get_user_model()


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)
