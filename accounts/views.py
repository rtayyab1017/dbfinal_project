from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from books.models import PersonExtend

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if  request.POST['pass'] == request.POST['re_pass']:
            if User.objects.filter(username=request.POST['email']).exists():
                return render(request, 'accounts/signup.html', {'error': 'Email already exists'})
                return redirect('signup')
            else:
                user = User.objects.create_user(username=request.POST['email'], password = request.POST['pass'],first_name=request.POST['first_name'],last_name= request.POST['last_name'])
                newperson = PersonExtend(user=user,checkoutdate=default,returndate=default)
                newperson.save()
                user.save()
                return redirect('login')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password are not Matching'})
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['email'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid Credentials'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
        auth.logout(request)
        return redirect('home')
