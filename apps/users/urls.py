from django.urls import path

from .views import UserCreateView, UserListView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/list', UserListView.as_view())
]
