from django.urls import path
from .  import views

urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('register/',views.regPage,name="register"),
    path('', views.home, name="home"),
]
