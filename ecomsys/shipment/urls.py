from django.urls import path
from shipment.views import ShippingDetailsApiView

urlpatterns = [
    path("shipment/", ShippingDetailsApiView.as_view()),
]
