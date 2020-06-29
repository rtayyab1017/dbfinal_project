from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if  request.POST['pass'] == request.POST['re_pass']:
            try:
                user = User.objects.get(email=request.POST['email'])
                return render(request,'accounts/signup.html', {'error': 'Email has already been registred!!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['email'], password = request.POST['pass'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html', {'error': 'Password does not match'})
    else:
        return render(request, 'accounts/signup.html', {'signup': signup})


def login(request):
    if request.method == 'POST':
        user1 = auth.authenticate(email=request.POST['email'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Email or Password is wrong'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
