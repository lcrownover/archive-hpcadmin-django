from django import forms

class UserForm(forms.Form):
    firstname = forms.CharField(label="First Name", max_length=100)
    lastname = forms.CharField(label="Last Name", max_length=100)
    username = forms.CharField(label="Username", max_length=100)
    email = forms.EmailField(label="Email", max_length=254)
    is_pi = forms.BooleanField(label="User is PI")
