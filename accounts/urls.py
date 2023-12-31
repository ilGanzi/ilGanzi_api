from django.contrib import admin
from django.urls import path

from .views import AuthAPIView, RegisterAPIView, UserAPIView, FindIdAPIView, FindPwAPIView, PwResetAPIView
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('auth/', AuthAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('user/', UserAPIView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('findid/',FindIdAPIView.as_view()),
    path('findpw/', FindPwAPIView.as_view()),
    path('user/resetPw/', PwResetAPIView.as_view()),
]
