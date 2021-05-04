from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .decorators import unathenticated_user
from .forms import CreateUserForm


@login_required(login_url='/login')
def index(request):
    return render(request, 'shopify_images/index.html')


@unathenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('/login/')

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