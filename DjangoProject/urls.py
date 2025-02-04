
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('register/', include('accounts.urls')),

    #    path('admin/', admin.site.urls),
]
