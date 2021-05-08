from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .decorators import unathenticated_user, allowed_users
from .forms import CreateUserForm, ImageForm
from .models import Image


@login_required(login_url='/login')
# @allowed_users(allowed_roles=['admin'])
def index(request):
    form = postImage(request)
    all_public_images = Image.objects.all().filter(privacy="Public").order_by('-date_created')
    return render(request, 'shopify_images/index.html', {'form': form, 'all_public_images': all_public_images})


@login_required(login_url='/login')
def myImagesPage(request):
    form = postImage(request)
    all_user_images = Image.objects.all().filter(user=request.user).order_by('-date_created')
    return render(request, 'shopify_images/my_images.html', {'form': form, 'all_user_images': all_user_images})


@unathenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='user')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('/login')

    context = {'form': form}
    return render(request, 'shopify_images/register.html', context)


@unathenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Username OR password is incorrect")
            return render(request, 'shopify_images/login.html')
    context = {}
    return render(request, 'shopify_images/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/login')


def postImage(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            image_uploader = form.save(commit=False)
            image_uploader.user = request.user  # The logged-in user
            image_uploader.save()
            return redirect('/')
    else:
        form = ImageForm()
    return form
