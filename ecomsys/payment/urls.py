from django.urls import path
from payment.views import PaymentMethodListApiView

urlpatterns = [
    path("payment/", PaymentMethodListApiView.as_view()),
]
