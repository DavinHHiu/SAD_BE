from django.urls import path
from userapp.views import LoginUserApiView, RegisterUserApiView, UserProfileApiView

urlpatterns = [
    path("register/", RegisterUserApiView.as_view()),
    path("login/", LoginUserApiView.as_view()),
    path("profile/", UserProfileApiView.as_view()),
]
