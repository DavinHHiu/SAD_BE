from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from book import urls as book_urls
from cloth import urls as cloth_urls
from mobilephone import urls as mobilephone_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(book_urls)),
    path("api/", include(mobilephone_urls)),
    path("api/", include(cloth_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
