from django.shortcuts import render,  get_list_or_404, get_object_or_404, redirect
from recipe.models import Recipe
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    recipes = Recipe.objects.order_by('-recipe_date').filter(published=True)
    paginator = Paginator(recipes, 6)
    page = request.GET.get('page')
    recipe_per_page = paginator.get_page(page)

    data = {
        'recipes': recipe_per_page 
    }
    return render(request, 'recipe/index.html', data)


def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    show_recipe = {
        'recipe': recipe
    }

    return render(request, 'recipe/recipe.html', show_recipe)




def create_recipe(request):
    if request.method == 'POST':
        recipe_name = request.POST['recipe_name']
        ingredients = request.POST['ingredients']
        method_preparation = request.POST['method_preparation']
        time_of_preparation = request.POST['time_of_preparation']
        server = request.POST['server']
        category = request.POST['category']
        recipe_image = request.FILES['recipe_image']
        user = get_object_or_404(User, pk=request.user.id)
        recipe = Recipe.objects.create(user=user, recipe_name=recipe_name, ingredients=ingredients, method_of_preparation=method_preparation, time_of_preparation=time_of_preparation, serves=server, category=category, recipe_image=recipe_image)
        recipe.save
        return redirect('dashboard')
    else:
        return render(request, 'recipe/create_recipe.html')


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    return redirect('dashboard')


def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe_to_edit = {'recipe': recipe}
    return render(request, 'recipe/edit_recipe.html', recipe_to_edit)

def update_recipe(request):
    if request.method == 'POST':
        recipe_id = request.POST['recipe_id']
        recipe = Recipe.objects.get(pk=recipe_id)
        recipe.recipe_name = request.POST['recipe_name']
        recipe.ingredients = request.POST['ingredients']
        recipe.method_of_preparation = request.POST['method_of_preparation']
        recipe.time_of_preparation = request.POST['time_of_preparation']
        recipe.serves = request.POST['serves']
        recipe.category = request.POST['category']
        if 'recipe_image' in request.FILES:
            recipe.recipe_image = request.FILES['recipe_image']
        recipe.save()
        return redirect('dashboard')

