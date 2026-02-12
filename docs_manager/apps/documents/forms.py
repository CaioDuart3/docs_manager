from django import forms
from .models import Document, Comment

import os
from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    """Formulário para upload de documento"""

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
        file = self.cleaned_data.get('file')
        if not file:
            return file

        # 🔒 Tamanho máximo: 50MB
        max_size = 50 * 1024 * 1024
        if file.size > max_size:
            raise forms.ValidationError(
                f'Arquivo muito grande! Máx 50MB '
                f'({file.size / 1024 / 1024:.2f}MB)'
            )

        # 🧾 Extensões permitidas
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
    