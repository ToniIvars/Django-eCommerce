from django import forms
from django.contrib.auth.models import User

class ProfileForm(forms.Form):
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'placeholder':'Password (not required)', 'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email', 'class':'form-control'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'First name', 'class':'form-control'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Last name', 'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super(ProfileForm, self).__init__(*args, **kwargs)

        if user_id:
            user = User.objects.get(id=user_id)

            self.fields['password'].initial = user.password
            self.fields['email'].initial = user.email
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
        
        fields = ('password', 'email', 'first_name', 'last_name')
        for field in fields:
            self.fields[field].label = ''