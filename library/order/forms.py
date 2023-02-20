from django import forms
from book.models import Book
from authentication.models import CustomUser

def book_str_for_forms(self):
    return f'book id: {self.id} book name: {self.name},'

def user_str_for_forms(self):
    return f'user id: {self.id} user email: {self.email},'


class UserBookSelectForm(forms.Form):
    CustomUser.__str__ = user_str_for_forms
    Book.__str__ = book_str_for_forms
    users = forms.ModelChoiceField(label='Choose user', queryset=CustomUser.objects.all())
    books = forms.ModelChoiceField(label='Choose book', queryset=Book.objects.all())
    date_end = forms.IntegerField(label='Enter order end', min_value=1)
    field_order = ["users", "books", "date_end"]

class BookSelectForm(forms.Form):
    Book.__str__ = book_str_for_forms
    books = forms.ModelChoiceField(queryset=Book.objects.all())
    date_end = forms.IntegerField(label='Enter order end', min_value=1)

class OrderDelFormUser(forms.Form):
    CustomUser.__str__ = user_str_for_forms
    users = forms.ModelChoiceField(label='Choose user', queryset=CustomUser.objects.all())

class OrderDelForm(forms.Form):
    order = forms.IntegerField(label='Enter order ID for delete')
