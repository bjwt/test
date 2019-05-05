#coding=UTF-8
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect

def login_view(request):    
    if request.POST.has_key('username'):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)    
    #验证失败，暂时不做处理
    return  HttpResponseRedirect("/")

def logout_view(request):
    logout(request)
    return  HttpResponseRedirect("/")