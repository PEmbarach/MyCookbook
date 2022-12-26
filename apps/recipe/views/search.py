from recipe.models import Recipe
from django.shortcuts import render,  get_list_or_404, get_object_or_404, redirect


def search(request):
    """ Search bar to find a specific recipe by name """
    recipes = Recipe.objects.order_by('-recipe_date').filter(published=True)

    if 'search' in request.GET:
        search_name = request.GET['search']
        if search:
            recipes = recipes.filter(recipe_name__icontains=search_name)

    new_data = {
        'recipes': recipes
    }

    return render(request, 'recipe/search.html', new_data)
