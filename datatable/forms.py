from dataclasses import fields
from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'category']