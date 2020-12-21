from django.shortcuts import render,redirect

# Create your views here.
def menu(request):
    return render(request,'index.html')