from django.views import View
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


class Access(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                return render(request, "login.html", {"ok": False})
            login(request, user)
        return redirect("index")


@method_decorator(login_required, name="dispatch")
class GetOut(View):
    def get(self, request):
        logout(request)
        return redirect("access")


class Index(View):
    def get(self, request):
        return render(request, "index.html")
