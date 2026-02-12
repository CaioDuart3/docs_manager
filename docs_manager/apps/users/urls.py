from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    # rota de login usando a view genérica de login do Django, com template personalizado
    path('', auth_views.LoginView.as_view(
        template_name='users/login.html'
    ), name='login'),

    # rota de logout usando a view genérica de logout do Django
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

