from django.urls import path
from .views import register_page, login_page, register_user, login_user, logout_user

urlpatterns = [
    path('login', login_page, name="login"),
    path('register', register_page, name="register"),
    path('login-user', login_user, name="login-user"),
    path('register-user', register_user, name="register-user"),
    path('logout', logout_user, name="logout")

]