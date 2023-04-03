from django.shortcuts import render, redirect
from base.models import Users
from base.forms import UserForm
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def index(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Look up the user by email instead of username
        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            user = None

        if request.user.is_authenticated:
            print("You are authenticated")
            return redirect('home')
        else:
            auth_user = authenticate(request, email=email, password=password)
            print("You are not authenticated")

        # Authenticate the user using username and password
        if user is not None:
            auth_user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request.user, auth_user)
                return redirect('home')

        return render(request, 'base/index.html', {'error': 'Invalid credentials'})

    else:
        return render(request, 'base/index.html')


    if request.user.is_authenticated:
        return redirect('home')
    
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')

    #     try:
    #         user = Users.objects.get(email=email)
    #     except Users.DoesNotExist:
    #         user = None

    #     auth_user = authenticate(request, email=email, password=password)

    #     if user is not None:
    #         if auth_user is not None:
    #             login(request, auth_user)
    #             print("Login Successful!")
    #             return redirect('home')
    #         else:
    #             print("Invalid email or password.")
    #             return render(request, 'base/index.html', {'error': 'Invalid email or password.'})
    #     else:
    #         print("User does not exist.")
    #         return render(request, 'base/index.html', {'error': 'User does not exist.'})

    # return render(request, 'base/index.html')



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
#@login_required
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