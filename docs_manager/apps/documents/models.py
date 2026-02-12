from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    null=True,
    blank=True
    )

    file = models.FileField(
        upload_to='documents/',
        help_text="Arquivo armazenado em pasta local"
    )
    file_name = models.CharField(max_length=255, default='arquivo', help_text="Nome original do arquivo")
    file_size = models.BigIntegerField(default=0, help_text="Tamanho do arquivo em bytes")
    file_type = models.CharField(max_length=100, blank=True, default='', help_text="Tipo MIME do arquivo")
    file_extension = models.CharField(max_length=10, blank=True, default='', help_text="Extensão do arquivo")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

    def __str__(self):
        return self.title
    
    def get_file_size_display(self):
        """Retorna o tamanho do arquivo em formato legível"""
        size = self.file_size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} TB"

    
class Comment(models.Model):
    document = models.ForeignKey(Document, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"

    def __str__(self):
        return f'Comentário de {self.author} em {self.document.title}'
