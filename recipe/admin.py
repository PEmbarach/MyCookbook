from django.contrib import admin
from .models import Recipe


class RecipeList(admin.ModelAdmin):
    list_display = ('id', 'recipe_name', 'category', 'recipe_date',
                    'published')
    list_display_links = ('id', 'recipe_name')
    search_fields = ('recipe_name',)
    list_filter = ('category',)
    list_editable = ('published',)
    list_per_page = 2


admin.site.register(Recipe, RecipeList)
