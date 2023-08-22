from django.shortcuts import render
from app1.models import account

# Create your views here.
def index(request):
    return render(request,'index.html')
def chef(request):
    return render(request,'chef.html')

def login1(request):
    return render(request,'login.html')

def admin(request):
    return render(request,'admin.html')

def user(request):
    return render(request,'user.html')
def restur(request):
    return render(request,'restaurant.html')
