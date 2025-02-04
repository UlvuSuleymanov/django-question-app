from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse

def register_page(request):
    return render(request, "accounts/registration.html")

def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Bu kullanıcı adı zaten alınmış."}, status=400)
        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({"message": "Kayıt başarılı!"})
    else:
        return JsonResponse({"error": "Geçersiz istek!"}, status=400)