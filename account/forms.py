
from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm, fields
from django.forms.forms import Form
from django.forms.models import modelform_factory
from .models import UserProduct,UserDetail


class AddProduct(forms.ModelForm):
    class Meta:
        model=UserProduct
        fields = ['productname','producttype','serialnumber','Date_Of_Purchase']

class Createuserform(UserCreationForm):
    class Meta:
        model= User
        fields=['username','email','password1','password2']