from django import forms
from haystack.forms import SearchForm


class loginForm(forms.Form):
	username = forms.CharField(label='登录名',max_length=10,min_length=4)
	password = forms.CharField(label='密码',widget=forms.PasswordInput,min_length=10,max_length=20)