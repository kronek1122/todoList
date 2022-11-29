from django.shortcuts import render, redirect
from . import models
from django.urls import reverse

# Create your views here.
def add(request):
    if request.POST:
        creation_time = ''
        title = request.POST['title']
        todo_text = request.POST['todo_text']
        #piority = request.POST['piority']
        condition = False
        #user = User
        creation_time = creation_time
        models.ToDoItem.objects.create(title=title,todo_text=todo_text, condition=condition, creation_time=creation_time)
        return redirect(reverse('todo:home'))
    else:
        return render(request, 'todo/add.html')

def list(request):
    all_todoitems = models.ToDoItem.objects.all()
    context = {'all_todoitems': all_todoitems}
    return render(request, 'todo/home.html', context=context)
    
def delete(request):
    if request.POST:
        id = request.POST['id']
        try:
            models.ToDoItem.objects.get(id=id).delete()
            return redirect(reverse('todo:home'))
        except:
            print('wrong id')
            return redirect(reverse('todo:home'))
        else:
            return render(request, 'todo/delete.html')
