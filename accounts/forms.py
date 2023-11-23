from django import forms
from django.contrib.auth.models import User


class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = {
            'username': 'Никнейм',
            'email': 'электронная почта',
            'first_name': 'фамилия',
            'last_name': 'имя'
        }


class Auth_codeForm(forms.Form):
    code = forms.IntegerField(label="Код регистрации")
