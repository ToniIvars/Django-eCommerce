from django import forms
from django.contrib.auth.models import User
from .models import Product

class ProfileForm(forms.Form):
    password = forms.CharField(label='', required=False, widget=forms.PasswordInput(attrs={'placeholder':'Password (not required)', 'class':'form-control'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder':'Email', 'class':'form-control'}))
    first_name = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'First name', 'class':'form-control'}))
    last_name = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'Last name', 'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super(ProfileForm, self).__init__(*args, **kwargs)

        if user_id:
            user = User.objects.get(id=user_id)

            self.fields['email'].initial = user.email
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

class ProductForm(forms.ModelForm): 
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'image')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Name', 'class':'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder':'Price', 'class':'form-control'}),
            'description': forms.Textarea(attrs={'placeholder':'Description of the product', 'class':'form-control'})
        }
        
        labels = {
            'name': '',
            'price': '',
            'description': ''
        }

class BuyForm(forms.Form):
    paying_way_choices = [
        ('bank_card', 'Bank card'),
        ('paypal', 'PayPal'),
        ('bitcoin', 'Bitcoin')
    ]

    address = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'placeholder':'Address', 'class':'form-control'}))
    paying_ways = forms.CharField(widget=forms.RadioSelect(choices=paying_way_choices))
    paying_data = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control'}))
    quantity = forms.IntegerField(label='', min_value=1, initial=1, widget=forms.NumberInput(attrs={'placeholder':'Number of products', 'class':'form-control'}))