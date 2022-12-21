from django.shortcuts import render,  get_list_or_404, get_object_or_404
from .models import Recipe


def index(request):
    recipes = Recipe.objects.all()

    data = {
        'recipes': recipes
    }
    return render(request, 'index.html', data)


def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    show_recipe = {
        'recipe': recipe
    }

    return render(request, 'recipe.html', show_recipe)
