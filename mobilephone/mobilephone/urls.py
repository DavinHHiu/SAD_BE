from django.contrib import admin
from django.urls import include, path
from mobilephoneapp import urls as mobilephoneapp_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(mobilephoneapp_urls)),
]
