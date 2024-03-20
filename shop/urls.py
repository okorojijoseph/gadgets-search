from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("login/", views.LoginPageView.as_view(), name="login"),
    path("token/", views.TokenView.as_view(), name="token"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("about/", views.AboutView.as_view(), name="about"),
]
