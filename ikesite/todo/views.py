from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import Todo
from .forms import TodoForm

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        form = TodoForm()  # initialize the form
        todos = Todo.objects.filter(user=request.user)  # filter only the Todo items for the current user
        ctx = {'todo_list': todos, 'form': form}  # form included in the context
        return render(request, 'todo/todo_list.html', ctx)

    def post(self, request):
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)  # not save yet
            todo.user = request.user  # set user to the current logged-in user
            todo.save()  # save the Todo
            return redirect('todo:todo_list')  # redirect to the same page to show the updated list
        todos = Todo.objects.filter(user=request.user)  # filter only the Todo items for the current user
        ctx = {'todo_list': todos, 'form': form}  # form included in the context
        return render(request, 'todo/todo_list.html', ctx)

class OpenView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')  # redirect to the login page if the user is not authenticated
        return render(request, 'todo/logout_view.html')  # otherwise show the logout page

class DeleteTodoView(View):
    def post(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)  # get the Todo item by primary key (pk)
        todo.delete()  # Delete the Todo item
        return redirect('todo:todo_list')  # redirect to the list view after deletion

class UpdateTodoView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)  # get the Todo item by primary key (pk)
        form = TodoForm(instance=todo)  # Pre-fill the form with the current Todo data
        ctx = {'form': form, 'todo': todo}
        return render(request, 'todo/update_todo.html', ctx)  # render the update form

    def post(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)  # get the Todo item by primary key (pk)
        form = TodoForm(request.POST, instance=todo)  # bind the form to the existing Todo object
        if form.is_valid():
            form.save()  # save the updated Todo
            return redirect('todo:todo_list')  # Redirect to the Todo list after updating
        ctx = {'form': form, 'todo': todo}
        return render(request, 'todo/update_todo.html', ctx)  # render the form with errors if any

