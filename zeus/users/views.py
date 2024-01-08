from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.decorators import login_required
from users.models import User, Profile
from django.contrib import messages


@login_required(login_url="login")
def home(request):
    return render(request, "pages/home.html", {})


def signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect("signup")
            elif User.objects.filter(name=username).exists():
                messages.info(request, "Email Already Taken")
                return redirect("signup")
            else:
                user = User.objects.create_user(
                    name=username, email=email, password=password
                )
                user.save()
                # log user in redirect to settings page

                # create a Profile object for the new user
                user_model = User.objects.get(email=email)
                new_profile = Profile.objects.create(user=user_model)
                new_profile.save()
                return redirect("home")
        else:
            messages.info(request, "Password Not Matching")
            return redirect("signup")
    else:
        return render(request, "pages/signup.html", {})


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(email=email, password=password)
        if user is not None:
            user_login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Credentials Invalid")
            return redirect("login")
    else:
        return render(request, "pages/login.html")


@login_required(login_url="login")
def logout(request):
    user_logout(request)
    return redirect("login")
