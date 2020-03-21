from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import *
from .forms import *


def index(request):
    todo_list = Task.objects.order_by('id')

    form = TodoForm()

    context = {
    	'todo_list' : todo_list,
    	'form' : form,
    }

    return render(request, 'todo/index.html', context)

@require_POST
def add(request):
	form = TodoForm(request.POST)

	if form.is_valid():
		new_task = Task(text=request.POST['text'])
		new_task.save()

	return redirect('index')


def complete(request, todo_id):
	task = Task.objects.get(pk=todo_id)
	task.complete = True
	task.save()

	return redirect('index')

def notcomplete(request, todo_id):
	task = Task.objects.get(pk=todo_id)
	task.complete = False
	task.save()	

	return redirect('index')

def delete(request, todo_id):
	task = Task.objects.get(pk=todo_id)
	task.delete()

	return redirect('index')

def delete_all(request):
	Task.objects.all().delete()

	return redirect('index')
