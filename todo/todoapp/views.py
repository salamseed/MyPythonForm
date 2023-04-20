from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import DailyTask
from .forms import updateform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class display(ListView):
    model = DailyTask
    template_name = 'home.html'
    context_object_name = 'details'


class detail(DetailView):
    model = DailyTask
    template_name = 'Detail.html'
    context_object_name = 'details'


class updateview(UpdateView):
    model = DailyTask
    template_name = 'updateview.html'
    context_object_name = 'details'
    fields = ('task', 'priority', 'date')
    def get_success_url(self):
        return reverse_lazy('todoapp:detail', kwargs={'pk': self.object.id})


class deleteview(DeleteView):
    model = DailyTask
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:home')


def displayhome(request):
    details = DailyTask.objects.all()
    if request.method == 'POST':
        task = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date','')
        work = DailyTask(task=task, priority=priority, date=date)
        work.save()
    return render(request, 'home.html', {'details': details})


def delete(request,id):
    if request.method == 'POST':
        slno = DailyTask.objects.get(id=id)
        slno.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request,id):
    data=DailyTask.objects.get(id=id)
    input=updateform(request.POST or None, instance=data)
    if input.is_valid():
        input.save()
        return redirect('/')
    return render(request,'update.html',{'data': data, 'input':input})


