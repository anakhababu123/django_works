from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from social.models import Post

class RegistraionForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name",
                "last_name",
                "username",
                "email",
                "password1",
                "password2"
                ]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["post",
                "image"]
        widgets={
            "post":forms.Textarea(attrs={"class":"form-control","rows":3}),
            "image":forms.FileInput(attrs={"class":"form-select"})
        }