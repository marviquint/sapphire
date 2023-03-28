from django.shortcuts import render, redirect
from base.models import Employee
from base.forms import EmployeeForm

# Create your views here.

def index(request):
    return render(request, 'base/index.html')

def otp(request):
    return render(request, 'base/otp.html')

def sample(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('index')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'base/sample.html', {'form': form})

def home(request):
    return render(request, 'base/home.html')

def url(request):
    return render(request, 'base/url.html')