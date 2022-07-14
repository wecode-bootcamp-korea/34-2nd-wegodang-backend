from django.urls import path

from users.views import KaKaoSignUpView, ProfileView

urlpatterns = [
    path('/kakao', KaKaoSignUpView.as_view()),
    path('/profile', ProfileView.as_view())
]