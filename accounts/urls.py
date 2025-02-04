from django.urls import path
from .views import register_user, register_page

urlpatterns = [
    path('', register_page, name="register_page"),
    path('add', register_user, name="register_user")
]