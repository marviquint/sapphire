from django.shortcuts import render, redirect
from base.models import Users
from base.forms import UserForm
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Users.objects.get(username=email)
        except:
            messages.error(request, 'User Does not Exists!')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            index(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password Does not Exists!')
    context = {"page": page}
    return render(request, 'base/index.html', context)

def otp(request):
    return render(request, 'base/otp.html')

# def sample(request):
#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('index')
#             except:
#                 pass
#     else:
#         form = EmployeeForm()
#     return render(request, 'base/sample.html', {'form': form})

def home(request):
    return render(request, 'base/home.html')

def url(request):
    return render(request, 'base/url.html')

def search(request):
    return render(request, 'base/searchtool.html')

def addUser(request):
    users = Users.objects.filter().exclude(userType='Admin')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form = form.save(commit=False)
                #form.password = form.generate_password()
                form.password = str(random.randint(1, 1000000))
                form.userType = "User"
                form.save()
                return redirect('adduser')
            except:
                pass
    else:
        form = UserForm()
    return render(request, 'base/add_user.html', {'users':users,'form': form})