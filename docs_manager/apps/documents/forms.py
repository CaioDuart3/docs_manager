from django import forms
from .models import Document, Comment

class DocumentForm(forms.Form):
    """Formulário customizado para upload de documento no banco"""
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Título do documento'
        })
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Descrição (opcional)'
        })
    )
    file = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.pdf,.doc,.docx,.txt,.xlsx,.csv'
        })
    )
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            # Validar tamanho máximo (25MB para banco de dados)
            max_size = 25 * 1024 * 1024
            if file.size > max_size:
                raise forms.ValidationError(
                    f'Arquivo muito grande! Máximo 25MB, você enviou {file.size / 1024 / 1024:.2f}MB'
                )
            
            # Validar extensão
            allowed_extensions = ['pdf', 'doc', 'docx', 'txt', 'xlsx', 'csv']
            file_extension = file.name.split('.')[-1].lower()
            if file_extension not in allowed_extensions:
                raise forms.ValidationError(
                    f'Tipo de arquivo não permitido! Extensões aceitas: {", ".join(allowed_extensions)}'
                )
        
        return file

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
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
    