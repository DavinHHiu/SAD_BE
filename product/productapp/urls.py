from django.urls import path
from productapp.views import ProductListApiView, ProductDetailApiView, ProductApiView

urlpatterns = [
    path("product/<str:product_id>", ProductApiView.as_view()),
    path("products/", ProductListApiView.as_view()),
    path("products/<str:product_id>", ProductDetailApiView.as_view()),
]
