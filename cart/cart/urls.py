from cartapp import urls as cartapp_urls
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(cartapp_urls)),
]
