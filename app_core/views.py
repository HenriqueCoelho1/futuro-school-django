from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


def access(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                return render(request, "login.html", {"ok": False})
            login(request, user)
        return redirect("login")
    return render(request, "login.html")


@login_required
def getout(request):
    logout(request)
    return redirect("login")
