from django.views.generic import ListView, DetailView
from .models import Dessert
from django.db.models import Q


class DessertListView(ListView):
    model = Dessert
    context_object_name = "dessert_list"
    template_name = "desserts/dessert_list.html"


class DessertDetailView(DetailView):
    model = Dessert
    context_object_name = "dessert"
    template_name = "desserts/dessert_detail.html"


class SearchResultsListView(ListView):
    model = Dessert
    context_object_name = "dessert_list"
    template_name = "desserts/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Dessert.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
