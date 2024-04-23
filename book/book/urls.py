from bookapp import urls as bookapp_urls
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(bookapp_urls)),
]
