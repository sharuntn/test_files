from django.shortcuts import render

# Create your views here.
def loginPage(request):
    return render(request,'loginpage/login.html')

def regPage(request):
    return render(request,'loginpage/register.html')

def home(request):
    return render(request,'loginpage/index.html')