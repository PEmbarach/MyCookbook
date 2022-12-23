from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from recipe.models import Recipe


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if not empty_field(name):
            messages.error(request, 'The name field cannot be blank.')
            return redirect('signup')
        if not empty_field(email):
            messages.error(request, 'The email field cannot be blank.')
            return redirect('signup')
        if password_not_match(password, password2):
            messages.error(request, 'The passwords are not the same')
            return redirect('signup')
        if User.objects.filter(username=name).exists():
            messages.error(request, 'User already registered')
            return redirect('signup')
        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        print('User success')
        messages.success(request, 'Signup successefully')
        return redirect('login')
    else:
        return render(request, 'final_user/signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email == '' or password == '':
            messages.error(request, 'The fields cannot be blank.')
            return redirect('login')
        print(email, password)
        if User.objects.filter(email=email).exists():
            name = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=name, password=password)
            if user is not None:
                auth.login(request, user)
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


def empty_field(field):
    return not field.strip()


def password_not_match(password, password2):
    return password != password2