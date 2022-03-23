from django.shortcuts import render


def user(request):
    template_name = "teste.html"
    return render(request, template_name)
