"""
forms.py

Define os formulários da aplicação para criação de documentos e comentários.

Formulários disponíveis:
- DocumentForm: usado para upload e validação de documentos.
- CommentForm: usado para criar comentários associados a documentos.

Notas:
    - O DocumentForm inclui validação de tamanho máximo de arquivo (50MB)
      e checagem de extensões permitidas.
    - O CommentForm usa widgets personalizados para melhor UX.
"""

import os
from django import forms
from .models import Document, Comment


class DocumentForm(forms.ModelForm):
    """
    Formulário para upload de documentos.

    Campos:
        title: título do documento.
        description: descrição opcional.
        file: arquivo a ser enviado.

    Validações:
        - Tamanho máximo do arquivo: 50MB.
        - Extensões permitidas: pdf, doc, docx, txt, xlsx, csv, jpg, jpeg, png, gif.
    """
    class Meta:
        model = Document
        fields = ['title', 'description', 'file']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título do documento'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descrição (opcional)'
            }),
            'file': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': (
                    '.pdf,.doc,.docx,.txt,.xlsx,.csv,'
                    '.jpg,.jpeg,.png,.gif'
                )
            })
        }

    def clean_file(self):
        """
        Valida o arquivo enviado pelo usuário.

        - Verifica se o arquivo não excede 50MB.
        - Verifica se a extensão do arquivo está entre as permitidas.
        
        Raises:
            forms.ValidationError: se o arquivo for maior que 50 mb ou tiver extensão inválida.

        Returns:
            UploadedFile: arquivo validado.
        """
        file = self.cleaned_data.get('file')
        if not file:
            return file

        # tamanho máximo: 50MB
        max_size = 50 * 1024 * 1024
        if file.size > max_size:
            raise forms.ValidationError(
                f'Arquivo muito grande! Máx 50MB '
                f'({file.size / 1024 / 1024:.2f}MB)'
            )

        # extensões permitidas
        allowed_extensions = {
            'pdf', 'doc', 'docx', 'txt', 'xlsx', 'csv',
            'jpg', 'jpeg', 'png', 'gif'
        }

        ext = os.path.splitext(file.name)[1].lower().lstrip('.')

        if ext not in allowed_extensions:
            raise forms.ValidationError(
                'Tipo de arquivo não permitido! '
                f'Extensões aceitas: {", ".join(sorted(allowed_extensions))}'
            )

        return file


class CommentForm(forms.ModelForm):
    """
    Formulário para criação de comentários em documentos.

    Campos:
        text: conteúdo do comentário.

    Widgets:
        - Textarea personalizado para melhor experiência do usuário.
    """
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Seu comentário'
            })
        }
