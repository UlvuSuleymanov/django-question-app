from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

@login_required(login_url='/auth/login')
def index(request):
    user_id = request.user.id
    print(f"Current user ID: {user_id}")
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})