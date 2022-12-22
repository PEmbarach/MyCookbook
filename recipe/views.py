from django.shortcuts import render,  get_list_or_404, get_object_or_404
from .models import Recipe


def index(request):
    recipes = Recipe.objects.order_by('-recipe_date').filter(published=True)

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


def search(request):
    recipes = Recipe.objects.order_by('-recipe_date').filter(published=True)

    if 'search' in request.GET:
        search_name = request.GET['search']
        if search_name:
            recipes = recipes.filter(recipe_name__icontains=search_name)

    new_data = {
        'recipe': recipes
    }

    return render(request, 'search.html', new_data)
