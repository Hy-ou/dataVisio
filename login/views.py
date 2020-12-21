from django.shortcuts import render,redirect
from . import models
from login.models import UserInfo
from django.http import HttpResponse

# Create your views here.
def login(request):
    ctx={}
    if request.method=='GET':
        return render(request,'login.html')
    username=request.POST.get('username')
    password=request.POST.get('password')
    print(username,password)

    user_obj=models.UserInfo.objects.filter(username=username,password=password).first()
    if not user_obj:
        ctx['rtl']="账户名或密码错误"
        return render(request,'login.html',ctx)
    else:
        rep=redirect('/index/')
        rep.set_cookie('is_login',True)
        return rep

def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    username=request.POST.get('username')
    password=request.POST.get('password')
    user_save=UserInfo(username=username,password=password)
    user_save.save()
    ctx={}
    ctx['rtl']="注册成功！"

    return render(request,'register.html',ctx)









