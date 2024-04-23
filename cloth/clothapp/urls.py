from clothapp.views import ClothDetailApiView, ClothListApiView
from django.urls import path

urlpatterns = [
    path("clothes/", ClothListApiView.as_view()),
    path("clothes/<int:cloth_id>", ClothDetailApiView.as_view()),
]
