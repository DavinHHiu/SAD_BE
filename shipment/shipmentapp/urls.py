from django.urls import path
from shipmentapp.views import ShippingDetailsApiView

urlpatterns = [
    path("shipment/", ShippingDetailsApiView.as_view()),
]
