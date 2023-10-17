from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from Auth_App.models import  User
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist.')
            return render(request, 'Auth_App/login.html')

        if user.check_password(password):
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, 'Login Successfully')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid login credentials.')
        else:
            messages.error(request, 'Incorrect password.')

        return render(request, 'Auth_App/login.html')

    return render(request, 'Auth_App/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def profile(request):
    user = request.user
    context = {
        'user' : user
    }
    return render(request, 'Auth_App/profile.html', context)