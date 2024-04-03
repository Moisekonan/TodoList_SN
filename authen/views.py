from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("pswd", None)

        user_verif = User.objects.filter(email=email).first()
        if user_verif:
            user = authenticate(
                request, username=user_verif.username, password=password
            )
            if user:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Mot de passe incorrect")
        else:
            messages.error(request, "L'utilisateur n'existe pas")
    return render(request, "authen/login.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        # TODO: you use the e-mail address and password to authenticate the user, 
        # check that the e-mail address is not being used
        email = request.POST.get("email", None)
        if User.objects.filter(email=email).exists():
            messages.error(request, "Cette adresse e-mail est déjà utilisée.")
            return render(request, "authen/register.html")
        
        password = request.POST.get("pswd", None)

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect("login")
        except Exception as e:  # TODO: get an exception and write the specific error message
            messages.error(request, f"Erreur lors de l'inscription: {str(e)}")
            return render(request, "authen/register.html")
    return render(request, "authen/register.html")


def logout_view(request):
    logout(request)
    return redirect("login")
