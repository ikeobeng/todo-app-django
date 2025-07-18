from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.

class HomeView(View):
    def get(self,request):
        host=request.get_host()
        islocal=host.find('localhost')>=0 or host.find('127.0.0.1')>=0
        context={'installed':settings.INSTALLED_APPS,'islocal':islocal}
        return render(request,'home/main.html',context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # save the user to the database
            login(request, user)  # log the user in
            return redirect('todo:todo_list')  # redirect to the todo list page
    else:
        form = UserCreationForm()  # if GET request, display an empty form
    return render(request, 'registration/register.html', {'form': form})
