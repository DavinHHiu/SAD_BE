from django.urls import path
from paymentapp.views import PaymentMethodListApiView

urlpatterns = [
    path("payment/", PaymentMethodListApiView.as_view()),
]
