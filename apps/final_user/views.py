from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from recipe.models import Recipe
from django.contrib.auth.models import User


def signup(request):
    """ Register a new user in the system """
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if empty_field(name):
            messages.error(request, 'The name field cannot be blank.')
            return redirect('signup')
        if empty_field(email):
            messages.error(request, 'The email field cannot be blank.')
            return redirect('signup')
        if password_not_match(password, password2):
            messages.error(request, 'The passwords are not the same')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'User already registered')
            return redirect('signup')
        if User.objects.filter(username=name).exists():
            messages.error(request, 'User already registered')
            return redirect('signup')
        user = User.objects.create_user(username=name, email=email,
                                        password=password)
        user.save()
        print('User success')
        messages.success(request, 'Signup successefully')
        return redirect('login')
    else:
        return render(request, 'final_user/signup.html')


def login(request):
    """ Log a user into the system """
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
    """ Logout a user into the system """
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    """ Directs the logged in user to a page for creating, viewing and editi
        their recipes """
    if request.user.is_authenticated:
        id = request.user.id
        recipes = Recipe.objects.order_by('-recipe_date').filter(user=id)

        data = {
            'recipes': recipes
        }

        return render(request, 'final_user/dashboard.html', data)
    else:
        return redirect('index')


def empty_field(field):
    """ Check that there is an empty field """
    return not field.strip()


def password_not_match(password, password2):
    """ Checks if the two given passwords are the same """
    return password != password2


def handler404(request, exception, template_name="404_error.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    return render(request, '500_error.html', status=500)
