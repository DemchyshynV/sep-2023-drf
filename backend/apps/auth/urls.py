from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth.views import RecoveryPasswordView, RecoveryRequestView, UserActivateView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_login'),
    path('/activate/<str:token>', UserActivateView.as_view()),
    path('/recovery', RecoveryRequestView.as_view()),
    path('/recovery/<str:token>', RecoveryPasswordView.as_view()),
]
