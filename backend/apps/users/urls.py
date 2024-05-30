from django.urls import path

from .views import TestEmailView, UserAddAvatarView, UserBlockView, UserListCreateView, UserUnBlockView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users_list_create'),
    path('/avatars', UserAddAvatarView.as_view()),
    path('/<int:pk>/block', UserBlockView.as_view()),
    path('/<int:pk>/unblock', UserUnBlockView.as_view()),
    path('/test', TestEmailView.as_view())
]
