from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register_page(request):
    return render(request, "authentication/registration.html")

def login_page(request):
    return render(request, "authentication/login.html")


def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)
        user = User.objects.create_user(username=username, email=email, password=password)
        return redirect("/auth/login")
    else:
        return JsonResponse({"error": "Geçersiz istek!"}, status=400)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")

            else:
                return JsonResponse({"error": "Account is disabled"}, status=400)
        else:
            return JsonResponse({"error": "Invalid username or password"}, status=400)
    else:
        return JsonResponse({"error": "Geçersiz istek!"}, status=400)

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")


