from django.shortcuts import render, redirect
from django.contrib.auth.models import User

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
    return render(request, 'final_user/login.html')


def logout():
    pass


def dashboard():
    pass
