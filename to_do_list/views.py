from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import AddNewForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    return render(request,'to_do_list/index.html',{'tasks':tasks})

def add_task(request):
    form = AddNewForm()

    if request.method == "POST":
        form = AddNewForm(request.POST)

    if form.is_valid():
        form.save(commit=True)
        return index(request)
    else:
        print("Form Invalid")

    return render(request,'to_do_list/add_task.html',{'form':form})

class TaskDelete(DeleteView):
    model = Task
    fields = ['task_name']
    success_url = reverse_lazy('to_do_list:index')
