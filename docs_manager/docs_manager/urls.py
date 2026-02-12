from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('documents/', include('apps.documents.urls')),
    path('users/', include('apps.users.urls')),
    path('', RedirectView.as_view(url='/users/', permanent=True)),  # redireciona "/" para "/users/"
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
