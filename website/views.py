from django.shortcuts import render
from django.http import HttpResponse
from .models import menu_item


# Create your views here.

def index(request):
    return HttpResponse('''
    <h1> hello world</h1>
    <h2> hello world</h2>
    <h3> hello world</h3>
    <h4> hello world</h4>
    <h5> hello world</h5>
    <h6> hello world</h6>
    ''')


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'sign up.html')


def menu(request):
    data = menu_item.objects.all()
    return render(request, "menu.html", {'first': data})
