from django.shortcuts import render
from django.views import View

from shop.models import Product


class LoginView(View):
    def get(self, request):
        context = {}
        return render(request, "shop/login.html", context=context)


class HomeView(View):
    def get(self, request):
        products = Product.objects.filter(user__is_superuser=True)[:6]
        context = {"products": products}
        return render(request, "shop/home.html", context=context)


class AboutView(View):
    def get(self, request):
        context = {}
        return render(request, "shop/about.html", context=context)
