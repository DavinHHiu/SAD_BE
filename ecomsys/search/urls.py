from django.urls import path
from search.views import SearchApiView

urlpatterns = [
    path("search/<str:keyword>", SearchApiView.as_view()),
    path("search/", SearchApiView.as_view()),
]
