from django.urls import path

from users.views import KaKaoLoginView

urlpatterns = [
    path('/signup', KaKaoLoginView.as_view()),
]