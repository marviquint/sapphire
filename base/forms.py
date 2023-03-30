from django import forms 
from base.models import Users
import random

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['employeeID', 'firstName', 'lastName', 'email', 'password', 'otp', 'userType']
        widgets = { 'employeeID': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Employee ID' } ),
            'firstName': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'First Name' }), 
            'lastName': forms.TextInput(attrs={ 'class': 'form-control',  'placeholder': 'Last Name' }),
            'email': forms.EmailInput(attrs={ 'class': 'form-control',  'placeholder': 'Email' }),
      }
