from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.documents_list, name='documents_list'),
    path('upload/', views.documents_upload, name='documents_upload'),
    path('<int:pk>/', views.documents_details, name='documents_details'),
    path('<int:pk>/delete/', views.documents_delete, name='documents_delete'),
    path('<int:pk>/download/', views.documents_download, name='documents_download'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
