from django.contrib import admin
from django.urls import include, path
from paymentapp import urls as paymentapp_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(paymentapp_urls)),
]
