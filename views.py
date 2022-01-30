from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("This is Homepage (/)")


def about(request):
    return HttpResponse("This is About page (/about)")


def projects(request):
    return HttpResponse("This is Project Page (/projects)")


def contacts(request):
    return HttpResponse("This is my Contact page (/contact)")
