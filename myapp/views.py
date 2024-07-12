from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem

def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'index.html', {'todos': todos})

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        todo = TodoItem.objects.create(title=title, description=description)
        return redirect('index')
    return render(request, 'create.html')

def toggle_complete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('index')

def delete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    todo.delete()
    return redirect('index')