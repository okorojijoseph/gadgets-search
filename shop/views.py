from django.conf import settings
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .mixins import LogoutRequiredMixin

from .auth import Google, register_social_user
from .models import Product


class LoginPageView(LogoutRequiredMixin, View):
    def get(self, request):
        context = {}
        return render(request, "shop/login.html", context=context)

class TokenView(LogoutRequiredMixin, View):
    def get(self, request):
        auth_token = request.GET.get("auth_token")
        user_data = Google.validate(auth_token)
        try:
            user_data["sub"]
        except:
            # Invalid auth token
            return redirect("/")
        if user_data["aud"] != settings.GOOGLE_CLIENT_ID:
            # Invalid client id
            return redirect("/")
        user = register_social_user(
            user_data["email"], user_data["name"], user_data["picture"]
        )
        login(request, user)
        return redirect("/")


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("/")


class HomeView(View):
    def get(self, request):
        products = Product.objects.filter(user__is_superuser=True)[:6]
        context = {"products": products}
        return render(request, "shop/home.html", context=context)


class AboutView(View):
    def get(self, request):
        context = {}
        return render(request, "shop/about.html", context=context)
