
from django.http import JsonResponse
from django.shortcuts import render
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
        return JsonResponse({"message": "User saved!"})
    else:
        return JsonResponse({"error": "Geçersiz istek!"}, status=400)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username  exists"}, status=200)
        return None
    else:
        return JsonResponse({"error": "Geçersiz istek!"}, status=400)



