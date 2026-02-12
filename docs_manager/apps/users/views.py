# from django.shortcuts import redirect, render
# from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.decorators import login_required

# def login(request):
#     return render(request, 'users/login.html')

# @login_required
# def logout(request):
#     auth_logout(request)  # Faz logout
#     return redirect('login')  