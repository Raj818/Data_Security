from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1', 'password2']

class UploadForm(forms.ModelForm):
    class Meta:
        model=upload_file
        fields = ['file_name', 'file']        