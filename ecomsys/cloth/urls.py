from django.urls import path

from cloth.views import ClothDetailApiView, ClothListApiView

urlpatterns = [
    path("clothes/", ClothListApiView.as_view()),
    path("clothes/<int:cloth_id>", ClothDetailApiView.as_view()),
]
