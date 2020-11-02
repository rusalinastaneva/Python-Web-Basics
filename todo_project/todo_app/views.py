from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from todo_app.forms import TodoForm
from todo_app.models import Todo


def index(request, form=None, form_action='create todo', pk=None):
    if not form:
        form = TodoForm()
    context = {
        'todos': Todo.objects.all().order_by('title'),
        'todo_form': form,
        'form_action': form_action,
        'pk': pk,
    }
    return render(request, 'index.html', context)


@require_POST
def create_todo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        todo = Todo(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            is_done=False)
        todo.save()
        return redirect('todos index')

    return index(request, form)


def edit_todo(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == "GET":
        form = TodoForm(instance=todo)
        return index(request, form, 'edit todo', pk=pk)
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            todo.title = form.cleaned_data['title']
            todo.description = form.cleaned_data['description']
            todo.save()
        return index(request, form)


@require_POST
def mark_todo_done(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = not todo.is_done
    todo.save()
    return redirect('todos index')


def delete_todo(request):
    pass