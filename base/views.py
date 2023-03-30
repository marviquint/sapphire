from django.shortcuts import render, redirect
from base.models import Users
from base.forms import UserForm
import random

# Create your views here.

def index(request):
    return render(request, 'base/index.html')

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