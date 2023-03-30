import random
from django import forms

class PasswordGeneratorForm(forms.Form):
    password_length = forms.IntegerField(min_value=8, max_value=64, initial=12, help_text="Enter password length (min 8, max 64)")

    def generate_password(self):
        length = self.cleaned_data.get('password_length')
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{};:,.<>?'
        password = ''.join(random.choice(chars) for _ in range(length))
        return password