from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import FileResponse, Http404
from .models import Document, Comment
from .forms import DocumentForm, CommentForm
from django.contrib.auth.decorators import login_required
import os

def can_delete_document(user, document):
    """
    Verifica se um usuário tem permissão para deletar um documento.
    - Administradores/staff podem deletar qualquer documento
    - Usuários comuns só podem deletar seus próprios documentos
    """
    if user.is_staff or user.is_superuser:
        return True
    return document.author == user

@login_required
def documents_list(request):
    documents = Document.objects.all()
    
    # Busca por título
    search = request.GET.get('search')
    
    if search:
        documents = documents.filter(title__icontains=search)
    
    return render(request, 'documents/documents_list.html', {
        'documents': documents,
        'current_user': request.user
    })

@login_required
def documents_details(request, pk):
    document = get_object_or_404(Document, pk=pk)
    comments = Comment.objects.filter(document=document)
    comment_form = CommentForm()
    
    # Verificar permissão para deletar
    can_delete = can_delete_document(request.user, document)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.document = document
            comment.author = request.user  # Atribua o objeto User diretamente
            comment.save()
            messages.success(request, 'Comentário adicionado com sucesso!')
            return redirect('documents_details', pk=document.pk)
        else:
            messages.error(request, 'Erro ao adicionar comentário. Verifique os dados.')
    
    return render(request, 'documents/documents_details.html', {
        'document': document,
        'comments': comments,
        'form': comment_form,
        'can_delete': can_delete
    })
@login_required
def documents_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Salvar o formulário (Django cuida de salvar o arquivo na pasta local)
                print("Salvando documento...")
                document = form.save(commit=False)
                document.author = request.user
                
                # Salvar metadados do arquivo
                if request.FILES.get('file'):
                    file_obj = request.FILES['file']
                    document.file_name = file_obj.name
                    document.file_size = file_obj.size
                    document.file_type = file_obj.content_type
                    document.file_extension = os.path.splitext(file_obj.name)[1].lower()
                
                # Salvar no banco de dados
                document.save()
                
                messages.success(
                    request, 
                    f'Documento "{document.title}" salvo com sucesso! ({document.get_file_size_display()})'
                )
                return redirect('documents_list')
            
            except Exception as e:
                messages.error(request, f'Erro ao salvar o documento: {str(e)}')
                print(f"Erro no upload: {e}")
        else:
            print("Formulário inválido:", form.errors)
            # Mostrar erros de validação
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = DocumentForm()
    
    return render(request, 'documents/documents_upload.html', {'form': form})

@login_required
def documents_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    
    # Verificar permissão
    if not can_delete_document(request.user, document):
        messages.error(request, 'Você não tem permissão para deletar este documento. Apenas o autor ou administradores podem deletá-lo.')
        return redirect('documents_details', pk=pk)
    
    if request.method == 'POST':
        try:
            title = document.title
            # Deletar arquivo da pasta local
            if document.file:
                document.file.delete()
            document.delete()
            messages.success(request, f'Documento "{title}" deletado com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro ao deletar documento: {str(e)}')
            print(f"Erro na deleção: {e}")
    
    return redirect('documents_list')

@login_required
def documents_download(request, pk):
    """Download do arquivo armazenado em pasta local"""
    document = get_object_or_404(Document, pk=pk)
    
    try:
        # Abrir arquivo da pasta local
        response = FileResponse(document.file.open('rb'), as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{document.file_name}"'
        response['Content-Type'] = document.file_type or 'application/octet-stream'
        return response
    except Exception as e:
        messages.error(request, f'Erro ao fazer download: {str(e)}')
        return redirect('documents_details', pk=pk)
    

