from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .form import TodoForm
from .models import Task

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class TaskListView(ListView):
    model = Task
    template_name = 'Home.html'
    context_object_name = 'task2'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task1'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task3'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetails', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task1'
    success_url = reverse_lazy('todoapp:cbvhome')



def Home(request):
    task2 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)

        task.save()
    return render(request, 'Home.html', {'task2': task2})


#
# def details(request):
#     task=Task.objects.all()
#     return render(request,'Home.html',{'task':task})

# def delete(request, id):
#     task1 = Task.objects.get(id=id)
#     if request.method == 'POST':
#         task1.delete()
#         return redirect('/')
#     return render(request, 'delete.html')

#
# def update(request, id):
#     task3 = Task.objects.get(id=id)
#     f = TodoForm(request.POST or None, instance=task3)
#     if f.is_valid():
#         f.save()
#         # return redirect('/')
#     return render(request, 'edit.html', {'f': f, 'tesk3': task3})
