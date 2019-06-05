from django import forms
from .models import Login, Register, Image, Contact


class LoginForm(forms.ModelForm):
    class Meta():
         model = Login
         fields = ('username', 'password')


class RegisterForm(forms.ModelForm):
    class Meta():
         model = Register
         fields = ('name', 'username', 'email', 'mobile', 'password')


class ImageForm(forms.Form):
    imgfile=forms.ImageField()


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=('phone', 'message')
