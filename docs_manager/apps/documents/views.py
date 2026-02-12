from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import FileResponse
from io import BytesIO
from .models import Document, Comment
from .forms import DocumentForm, CommentForm
from django.contrib.auth.decorators import login_required
import os

@login_required
def documents_list(request):
    documents = Document.objects.all()
    
    # Busca por título
    search = request.GET.get('search')
    
    if search:
        documents = documents.filter(title__icontains=search)
    
    return render(request, 'documents/documents_list.html', {'documents': documents})

@login_required
def documents_details(request, pk):
    document = get_object_or_404(Document, pk=pk)
    comments = Comment.objects.filter(document=document)
    comment_form = CommentForm()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.document = document
            comment.save()
            messages.success(request, 'Comentário adicionado com sucesso!')
            return redirect('documents_details', pk=document.pk)
        else:
            messages.error(request, 'Erro ao adicionar comentário. Verifique os dados.')
    
    return render(request, 'documents/documents_details.html', {
        'document': document,
        'comments': comments,
        'form': comment_form
    })

@login_required
def documents_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Criar novo documento
                document = Document()
                document.title = form.cleaned_data['title']
                document.description = form.cleaned_data['description']
                
                # Ler o arquivo enviado e salvá-lo no banco como dados binários
                if request.FILES.get('file'):
                    file_obj = request.FILES['file']
                    
                    # Ler conteúdo do arquivo
                    file_content = file_obj.read()
                    
                    # Salvar como BinaryField
                    document.file = file_content
                    
                    # Salvar metadados
                    document.file_name = file_obj.name
                    document.file_size = file_obj.size
                    document.file_type = file_obj.content_type
                    document.file_extension = os.path.splitext(file_obj.name)[1].lower()
                
                # Salvar no banco de dados
                document.save()
                
                messages.success(
                    request, 
                    f'Documento "{document.title}" salvo no banco com sucesso! ({document.get_file_size_display()})'
                )
                return redirect('documents_list')
            
            except Exception as e:
                messages.error(request, f'Erro ao salvar o documento: {str(e)}')
                print(f"Erro no upload: {e}")
        else:
            # Mostrar erros de validação
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = DocumentForm()
    
    return render(request, 'documents/documents_upload.html', {'form': form})

def documents_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    
    if request.method == 'POST':
        try:
            title = document.title
            document.delete()
            messages.success(request, f'Documento "{title}" deletado com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro ao deletar documento: {str(e)}')
            print(f"Erro na deleção: {e}")
    
    return redirect('documents_list')

def documents_download(request, pk):
    """Download do arquivo armazenado no banco"""
    document = get_object_or_404(Document, pk=pk)
    
    try:
        # Criar resposta com o arquivo binário do banco
        response = FileResponse(BytesIO(document.file), as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{document.file_name}"'
        response['Content-Type'] = document.file_type or 'application/octet-stream'
        return response
    except Exception as e:
        messages.error(request, f'Erro ao fazer download: {str(e)}')
        return redirect('documents_details', pk=pk)