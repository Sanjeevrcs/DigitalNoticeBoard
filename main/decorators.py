from django.http import HttpResponse
from django.shortcuts import redirect

def unauth_user(func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('main')
        else:
            return func(request,*args,**kwargs)

    return wrapper_func