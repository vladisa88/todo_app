from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.base import View

from .models import Tasks
from .forms import TaskForm


class AllTodos(ListView):
    model = Tasks
    queryset = Tasks.objects.all()
    template_name = 'todo_list.html'


class AddTodo(View):

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

class UpdateTodo(View):
    def get(self, request, pk):
        task = Tasks.objects.get(id=pk)
        form = TaskForm(instance=task)
        context = {'form': form}
        return render(request, 'update_task.html', context)

    def post(self, request, pk):
        task = Tasks.objects.get(id=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

class DeleteTodo(View):
    def post(self, request, pk):
        task = Tasks.objects.get(id=pk)
        task.delete()
        return redirect('/')
