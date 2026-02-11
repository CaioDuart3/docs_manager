from django.shortcuts import render, redirect, get_object_or_404
from .models import Document, Comment
from .forms import DocumentForm, CommentForm

def documents_list(request):
    documents = Document.objects.all()
    return render(request, 'documents/documents_list.html', {'documents': documents})

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
            return redirect('documents_details', pk=document.pk)
    return render(request, 'documents/documents_details.html', {
        'document': document,
        'comments': comments,
        'form': comment_form
    })

def documents_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('documents_list')
    else:
        form = DocumentForm()
    return render(request, 'documents/documents_upload.html', {'form': form})

def documents_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('documents_list')
    return redirect('documents_list')