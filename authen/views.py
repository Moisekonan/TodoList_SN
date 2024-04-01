from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('pswd', None)

        user_verif = User.objects.filter(email=email).first()
        if user_verif:
            user = authenticate(
                request, username=user_verif.username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                print("mot de pass incorrecte")
        else:
            print("User does not exist")

    return render(request, 'authen/login.html', {})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('pswd', None)

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('login')
        except:
            return render(request, 'authen/register.html', {'error': 'User already exists'})
    return render(request, 'authen/register.html')


def logout_view(request):
    logout(request)
    return redirect('login')
