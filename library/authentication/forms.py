from django import forms

class UserRoleForm(forms.Form):
   enter_id = forms.IntegerField(label='Enter user ID')


class LoginForm(forms.Form):
   login = forms.CharField(label='Login')
   password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
   login = forms.CharField(label='Login')
   password = forms.CharField(widget=forms.PasswordInput)
   confirm_password = forms.CharField(widget=forms.PasswordInput)
   firstname = forms.CharField(label='Firstname')
   lastname = forms.CharField(label='Lastname')
   middle_name = forms.CharField(label='Lastname')
   role = forms.ChoiceField(label="Role", choices=((0, "Visitor"), (1, "Librarian")))
