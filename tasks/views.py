from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Count,Q
from django.views.decorators.http import require_POST
from .models import Task
from .forms import TaskForm,RegisterForm

def register(request):
 if request.user.is_authenticated:return redirect('task_list')
 form=RegisterForm(request.POST or None)
 if request.method=='POST' and form.is_valid():
  user=form.save();login(request,user);return redirect('task_list')
 return render(request,'registration/register.html',{'form':form})

@login_required
def task_list(request):
 qs=Task.objects.filter(owner=request.user)
 stats=qs.aggregate(total=Count('id'),done=Count('id',filter=Q(status='done')),progress=Count('id',filter=Q(status='progress')))
 status=request.GET.get('status','all')
 if status in ['todo','progress','done']:qs=qs.filter(status=status)
 search=request.GET.get('q','').strip()
 if search:qs=qs.filter(Q(title__icontains=search)|Q(description__icontains=search))
 return render(request,'tasks/list.html',{'tasks':qs,'stats':stats,'selected':status,'search':search})

@login_required
def task_create(request):
 form=TaskForm(request.POST or None)
 if request.method=='POST' and form.is_valid():
  task=form.save(commit=False);task.owner=request.user;task.save();return redirect('task_list')
 return render(request,'tasks/form.html',{'form':form,'heading':'Новая задача'})

@login_required
def task_edit(request,pk):
 task=get_object_or_404(Task,pk=pk,owner=request.user)
 form=TaskForm(request.POST or None,instance=task)
 if request.method=='POST' and form.is_valid():form.save();return redirect('task_list')
 return render(request,'tasks/form.html',{'form':form,'heading':'Редактировать задачу'})

@login_required
@require_POST
def task_delete(request,pk):
 get_object_or_404(Task,pk=pk,owner=request.user).delete()
 return redirect('task_list')
