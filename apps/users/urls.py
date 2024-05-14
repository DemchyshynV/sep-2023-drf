from django.urls import path

from .views import UserBlockView, UserListCreateView, UserUnBlockView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/<int:pk>/block', UserBlockView.as_view()),
    path('/<int:pk>/unblock', UserUnBlockView.as_view()),
]
