from django.contrib import admin
from django.urls import path, include
from shipmentapp import urls as shipment_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(shipment_urls)),
]
