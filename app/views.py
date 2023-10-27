from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.


def home_view(request: HttpRequest) -> render:
    return render(request, "home.html")


def management_view(request: HttpRequest) -> render:
    return render(request, "management.html")


def procurement_view(request: HttpRequest) -> render:
    return render(request, "procurement.html")


def documentation_view(request: HttpRequest) -> render:
    return render(request, "documentation.html")


def community_view(request: HttpRequest) -> render:
    return render(request, "community.html")
