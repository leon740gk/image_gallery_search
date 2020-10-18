from django.urls import path

from .views import SearchImagesView


urlpatterns = [
    path('<str:searchTerm>/', SearchImagesView.as_view(), name='search'),
]