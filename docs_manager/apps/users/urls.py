from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='users/login.html', next_page='documents_list'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/documents/'), name='logout'),
]
