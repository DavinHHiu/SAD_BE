from django.urls import path

from cart.views import CartListApiView

urlpatterns = [path("cart/", CartListApiView.as_view())]
