"""
models.py

Define os modelos principais da aplicação de gerenciamento de documentos:
- Document: representa um arquivo enviado por um usuário.
- Comment: representa comentários feitos em documentos por usuários.
"""

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import os


class Document(models.Model):
    """
    Representa um documento enviado por um usuário.

    Campos:
        title: título do documento.
        description: descrição opcional do documento.
        author: usuário que enviou o documento.
        file: arquivo armazenado na pasta 'documents/'.
        file_name: nome original do arquivo.
        file_size: tamanho do arquivo em bytes.
        file_type: tipo MIME do arquivo (ex: application/pdf).
        file_extension: extensão do arquivo (ex: .pdf, .docx).
        uploaded_at: data/hora de envio.
        updated_at: data/hora da última atualização.
    """
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
        """Retorna o título do documento."""
        return self.title
    
    def can_be_deleted_by(self, user):
        """
        Verifica se um usuário pode deletar este documento.

        Regras:
            - Administradores (staff ou superuser) podem deletar qualquer documento.
            - Usuários comuns só podem deletar documentos que eles mesmos enviaram.

        Args:
            user (User): Usuário a ser verificado.

        Returns:
            bool: True se o usuário pode deletar, False caso contrário.
        """
        if user.is_staff or user.is_superuser:
            return True
        return self.author == user
    
    def get_file_size_display(self):
        """
        Retorna o tamanho do arquivo em formato legível.

        Converte bytes em KB, MB, GB ou TB, dependendo do tamanho.

        Returns:
            str: Tamanho formatado, ex: '1.23 MB'.
        """
        size = self.file_size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} TB"


class Comment(models.Model):
    """
    Representa um comentário feito em um documento.

    Campos:
        document: documento ao qual o comentário pertence.
        author: usuário que escreveu o comentário.
        text: conteúdo do comentário.
        created_at: data/hora de criação do comentário.
    """
    document = models.ForeignKey(Document, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"

    def __str__(self):
        """Retorna uma string resumida do comentário."""
        return f'Comentário de {self.author} em {self.document.title}'
