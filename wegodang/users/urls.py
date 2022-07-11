from django.urls import path

from users.views import KaKaoSignUpView

urlpatterns = [
    path('/kakao', KaKaoSignUpView.as_view())
]