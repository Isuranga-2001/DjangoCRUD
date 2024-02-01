from django.shortcuts import render
from .models import User


# Create your views here.
def index(request):
    return render(request, "myapp/index.html", {})


def register(request):
    return render(request, "myapp/userReg.html", {})


def insert_user(request):
    uid = request.POST.get('uid')
    uname = request.POST.get('uname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    user = User(uid=uid, uname=uname, email=email, phone=phone)
    user.save()
    return render(request, "myapp/index.html", {})
