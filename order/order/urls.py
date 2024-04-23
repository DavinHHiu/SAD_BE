from django.contrib import admin
from django.urls import include, path
from orderapp import urls as order_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(order_urls)),
]
