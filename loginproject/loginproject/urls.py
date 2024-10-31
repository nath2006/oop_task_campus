from django.urls import path
from myapp.views import register, login_view, home, logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('logout/', logout_view, name='logout'),
]
