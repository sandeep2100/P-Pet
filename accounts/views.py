from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .helpers import send_forget_password_mail
import uuid
from .models import *

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username")
            return redirect("login")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Invalid Password")
            return redirect("login")

        else:
            login(request, user)
            messages.info(request, "Login Successfully")
            return redirect("login")

    return render(request, "user/login.html")


def logout_page(request):
    logout(request)
    return redirect("login")


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username Already Taken.")
            return redirect("register")

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully.")
        return redirect("register")
    return render(request, "user/register.html")


def ChangePassword(request, token):
    context = {}
    try:
       profile_obj = Profile.objects.get(forget_password_token=token)
       print(profile_obj)

    except Exception as e:
        print(e)
    return render(request, "change-password.html")



def ForgotPassword(request):
    try:
        if request.method == "POST":
            username = request.POST.get("username")

            if not User.objects.filter(username=username).first:
                messages.info(request, "No User Found with this username")
                return redirect("forgot-password")

            user_obj = User.objects.get(username=username)
            token = str(uuid.uuid4())
            send_forget_password_mail(user_obj, token)
            messages.info(request, "An Email is Sent")
            return redirect("forgot-password")

    except Exception as e:
        print(e)
    return render(request, "user/forget_password.html")

