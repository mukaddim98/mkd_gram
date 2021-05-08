from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from shopify_images.models import Image


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file_name', 'image', 'privacy', 'user']
        exclude = ['user']

