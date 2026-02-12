from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Rota de listagem de documentos
    path('', views.documents_list, name='documents_list'), 
    # Rota para upload de documentos
    path('upload/', views.documents_upload, name='documents_upload'),
    # Rota para exibir detalhes do documento, incluindo comentários e para adicionar comentários
    path('<int:pk>/', views.documents_details, name='documents_details'),
    # Rota para deletar documento
    path('<int:pk>/delete/', views.documents_delete, name='documents_delete'),
    # Rota para download do documento
    path('<int:pk>/download/', views.documents_download, name='documents_download'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
