from django.urls import path

from user.views import LoginUserApiView, RegisterUserApiView

urlpatterns = [
    path("register/", RegisterUserApiView.as_view()),
    path("login/", LoginUserApiView.as_view()),
]
