from django.contrib import admin
from .models import Dessert, Review


class ReviewInline(admin.TabularInline):
    model = Review


class DessertAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("title", "author", "ingredients",)


admin.site.register(Dessert, DessertAdmin)
