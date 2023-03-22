from django import forms
from Market.models import Display
from django.contrib.auth.models import User

class DisplayForm(forms.ModelForm):
    class Meta:
        model = Display
        fields = ['name','price','quantity']

# class CartForm(forms.ModelForm):
#     class meta:
#         model:AddToCart
#         fields=['cart']

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','email')