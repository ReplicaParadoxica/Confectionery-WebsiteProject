from django.urls import path
from .views import DessertListView, DessertDetailView, SearchResultsListView
urlpatterns = [
    path("", DessertListView.as_view(), name="dessert_list"),
    path("<uuid:pk>", DessertDetailView.as_view(), name="dessert_detail"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]
