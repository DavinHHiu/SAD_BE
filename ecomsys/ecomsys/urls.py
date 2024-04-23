from book import urls as book_urls
from cart import urls as cart_urls
from cloth import urls as cloth_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from mobilephone import urls as mobilephone_urls
from order import urls as order_urls
from payment import urls as payment_urls
from search import urls as search_urls
from shipment import urls as shipment_urls
from user import urls as user_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(book_urls)),
    path("api/", include(mobilephone_urls)),
    path("api/", include(cloth_urls)),
    path("api/", include(user_urls)),
    path("api/", include(cart_urls)),
    path("api/", include(search_urls)),
    path("api/", include(order_urls)),
    path("api/", include(payment_urls)),
    path("api/", include(shipment_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
