from django import forms
from .models import Book


class BookForm(forms.Form):
    name = forms.CharField(label='Name')
    description = forms.CharField(label='Description', widget=forms.Textarea)
    count = forms.IntegerField(label='Count', min_value=1)
