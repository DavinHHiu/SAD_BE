from django.urls import path

from mobilephone.views import MobilePhoneDetailApiView, MobilePhoneListApiView

urlpatterns = [
    path("mobile_phones/", MobilePhoneListApiView.as_view()),
    path("mobile_phones/<int:mobile_phone_id>", MobilePhoneDetailApiView.as_view()),
]
