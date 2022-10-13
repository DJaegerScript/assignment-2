import datetime
import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from todolist.Form import TodoListForm
from django.core import serializers

from todolist.models import TaskItem

# TODO: Create your views here.
@login_required(login_url='/todolist/login')
def show_todolist(request):
    task_items = TaskItem.objects.filter(user=request.user)
    context = {
        'task_items': task_items,
    }
    
    return render(request, "todolist.html", context)

def register_todolist(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('todolist:login_todolist')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_todolist(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # create response
            response.set_cookie('last_login', str(datetime.datetime.now())) # create last_login cookie and add it to response
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_todolist(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_todolist'))
    response.delete_cookie('last_login')
    return response

def create_todolist(request, id = 0):
    if request.method == 'POST':
        if id != 0:
            task_instance = TaskItem.objects.get(pk=id)
            task_instance.is_finished = not task_instance.is_finished
        else:
            form = TodoListForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                user = request.user
                date = datetime.datetime.now()
                task_instance = TaskItem(title=title, description=description, user=user, date=date)
        task_instance.save()
        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    
    context = { 'form': TodoListForm() }
    return render(request, 'create_todolist.html', context)

def delete_todolist(request, id):
    task_instance = TaskItem.objects.get(pk=id)
    task_instance.delete()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))

@login_required(login_url='/todolist/login')
def todolist(request):
    return render(request, "todolist_index.html")

def get_task(request):
    task_items = TaskItem.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', task_items))

def create_task(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        
        title = data.get('title')
        description = data.get('description')
        user = request.user
        date = datetime.datetime.now()
        
        task_instance = TaskItem(title=title, description=description, user=user, date=date)
        task_instance.save()
        
        data = {
            "message": 'Successfully submitted'
        }
        
        json_object = json.dumps(data, indent = 4) 

        return JsonResponse(json.loads(json_object))
    
    context = { 'form': TodoListForm() }
    return render(request, 'todolist_store.html', context)

def destroy_task(request, id):
    task_instance = TaskItem.objects.get(pk=id)
    task_instance.delete()
    data = {
        "message": 'Successfully deleted'
    }
        
    json_object = json.dumps(data, indent = 4) 

    return JsonResponse(json.loads(json_object))

def update_task(request, id):
    task_instance = TaskItem.objects.get(pk=id)
    task_instance.is_finished = not task_instance.is_finished
    task_instance.save()
    data = {
        "message": 'Successfully updated'
    }
        
    json_object = json.dumps(data, indent = 4) 

    return JsonResponse(json.loads(json_object))
