from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


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
        email = request.POST.get("email", None)
        password = request.POST.get("pswd", None)

        if User.objects.filter(email=email).exists():
            messages.error(request, "Cette adresse e-mail est déjà utilisée.")
            return render(request, "authen/register.html")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "ce nom d'utilisateur est déjà utilisée.")
            return render(request, "authen/register.html")

        try:
            validate_password(password)
        except ValidationError as error:
            messages.error(request, f"{', '.join(error.messages)}")
            return render(request, "authen/register.html")

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect("login")
        except Exception as e:
            messages.error(request, "Une erreur s'est produite lors de l'inscription.")
            return render(request, "authen/register.html")
    
    return render(request, "authen/register.html")



def logout_view(request):
    logout(request)
    return redirect("login")
