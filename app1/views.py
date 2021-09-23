from typing import Text
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
# from django.http import HttpResponse

# from django.http import redirect

# Create your views here.


def setcookies(request):
    response = render(request, "cookie.html")
    if request.COOKIES.get('visits'):
        response.set_cookie('data', 'Welcome Back')
        value = int(request.COOKIES.get('visits'))
        response.set_cookie('visits', value + 1)
    else:            
        value = 1
        text = "Welcome for the first time"
        response.set_cookie('visits', value)
        response.set_cookie('data', text)


    # response.set_cookie(key='name', value="Nilesh")
    # response.set_cookie(key='age', value="24")
    return response



def homepage(request):
    # print(request.COOKIES.items())
    return HttpResponse("Hello People, You are into the New Revolution of Technology...!")


def getcookie(request):
    nm = request.COOKIE.get('name')
    ag = request.COOKIE.get('age')
    print(nm, ag)    
    return render(request, "show_cookies.html")


def delete_cookies(request):
    response = redirect('home')
    response.delete_cookie('name')
    response.delete_cookie('age')
    return response


















