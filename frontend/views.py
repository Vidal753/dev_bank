from django.shortcuts import render


def IndexView(request):
    return render(request, "frontend/base.html")
