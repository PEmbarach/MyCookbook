from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from recipe.models import Recipe


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if not name.strip():
            print('The name field cannot be blank.')
            return redirect('signup')
        if not email.strip():
            print('The email field cannot be blank.')
            return redirect('signup')
        if password != password2:
            print('The passwords are not the same')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            print('User already registered')
            return redirect('signup')
        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        print('User success')
        return redirect('login')
    else:
        return render(request, 'final_user/signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email == '' or password == '':
            print('Os estao em branco')
            return redirect('login')
        print(email, password)
        if User.objects.filter(email=email).exists():
            name = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=name, password=password)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')

    return render(request, 'final_user/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        recipes = Recipe.objects.order_by('-recipe_date').filter(user=id)

        data = {
            'recipes': recipes
        }

        return render(request, 'final_user/dashboard.html', data)
    else:
        return redirect('index')


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
        return render(request, 'final_user/create_recipe.html')
