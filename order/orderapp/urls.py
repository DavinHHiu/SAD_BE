from django.urls import path
from orderapp.views import PlaceOrderApiView

urlpatterns = [
    path("order/", PlaceOrderApiView.as_view()),
]
