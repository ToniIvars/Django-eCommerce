from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'Password'}))