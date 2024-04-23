from cartapp.views import CartListApiView
from django.urls import path

urlpatterns = [path("cart/", CartListApiView.as_view())]
