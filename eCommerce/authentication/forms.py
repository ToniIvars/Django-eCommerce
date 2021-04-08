from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['password'].label = ""

class SignupForm(forms.Form):
    username = forms.CharField(required=True, max_length=20, widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'form-control'}))
    email = forms.EmailField(required=True, max_length=50, widget=forms.EmailInput(attrs={'placeholder':'Email', 'class':'form-control'}))
    password = forms.CharField(required=True, min_length=8, max_length=16, widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-control'}))
    password2 = forms.CharField(required=True, min_length=8, max_length=16, widget=forms.PasswordInput(attrs={'placeholder':'Password (again)', 'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['email'].label = ""
        self.fields['password'].label = ""
        self.fields['password2'].label = ""