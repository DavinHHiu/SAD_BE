from clothapp import urls as clothapp_urls
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(clothapp_urls)),
]
