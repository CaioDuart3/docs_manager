from django.shortcuts import render


def login(request):
    return render(request, 'users/login.html')

def logout(request):
    pass