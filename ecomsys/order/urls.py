from django.urls import path
from order.views import PlaceOrderApiView

urlpatterns = [
    path("order/", PlaceOrderApiView.as_view()),
]
