from django.urls import path
from . import views

urlpatterns = [
    path('', views.documents_list, name='documents_list'),
    path('upload/', views.documents_upload, name='documents_upload'),
    path('<int:pk>/', views.documents_details, name='documents_details'),
]
