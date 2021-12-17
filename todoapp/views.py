from django.shortcuts import render, redirect
from .models import TodoModel
from .forms import TodoForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import os
import slack

def signupfunc(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        raw_password = request.POST['password']
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            login(request, user)
            return redirect('list')            
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

def logoutfunc(request):
    logout(request)
    return redirect('login')

@login_required
def listfunc(request):
    object_list = TodoModel.objects.all()
    keyword = request.GET.get('keyword')
    sort = request.GET.get('sort')
    narrow = request.GET.get('narrow')
    if keyword:
        object_list = object_list.filter(
                 Q(title__icontains=keyword) | Q(memo__icontains=keyword)
               )
        # messages.success(request, '「{}」の検索結果'.format(keyword)) 
    if sort:
        object_list = object_list.order_by(sort)
    if narrow:
        object_list = object_list.filter(status__exact = narrow)
    # client = slack.WebClient(token=os.environ['xoxb-971829793847-2839825055731-ra5sXhos5p9zCWYXp2ZTJuuT'])
    # response = client.chat_postMessage(
    #     channel = '#random', # PostするChannel名
    #     text = "Postメッセージ"     # Postするメッセージ
    # )
    # assert response["ok"]
    # assert response["message"]["text"] == "Hello world!"

    return render(request, 'list.html', {'object_list':object_list})

@login_required
def detailfunc(request, pk):
    object = TodoModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})

# def createfunc(request):
#     if request.method == "POST":
#         object_list = request.POST
#         return redirect('list')
#     else:
#         return render(request, 'create.html', {})

@login_required
def createfunc(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        user = request.user.id
        if form.is_valid():
            object = form.save(commit=False)
            object.user_id = user
            object.save()
            return redirect('detail', pk=object.pk)
    else:
        form = TodoForm()
    return render(request, 'create.html', {'form': form})

@login_required
def deletefunc(request, pk):
    if request.method == "POST":
        object = TodoModel.objects.get(pk=pk)
        object.delete()
        return redirect(('list'))
    else:
        object = TodoModel.objects.get(pk=pk)
    return render(request, 'delete.html', {})

@login_required
def updatefunc(request, pk):
    object = TodoModel.objects.get(pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            object = form.save(commit=True)
            return redirect('detail', pk=object.pk)
    else:
        form = TodoForm(instance=object)
        return render(request, 'update.html', {'form': form, 'object': object})

