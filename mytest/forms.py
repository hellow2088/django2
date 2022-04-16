from django import forms
from django.forms import widgets


class registerForm(forms.Form):
	username = forms.CharField(max_length=10,min_length=4,label='用户名',widget=widgets.TextInput(attrs={'class':'form-control'},))
	password = forms.CharField(max_length=20,min_length=6,label='密码',widget=forms.PasswordInput(attrs={'class':'form-control'},))
	repassword = forms.CharField(max_length=20,min_length=6,label='确认密码',widget=forms.PasswordInput(attrs={'class':'form-control'},))
	emial = forms.CharField(max_length=30,min_length=15,label='邮箱',widget=widgets.EmailInput(attrs={'class':'form-control'},))


class loginForm(forms.Form):
	username = forms.CharField(max_length=10,label='用户名')
	password = forms.CharField(max_length=20,label='密码',widget=forms.PasswordInput)


class cgpwdForm(forms.Form):
	username = forms.CharField(label='用户名')
	password = forms.CharField(label='密码',widget=forms.PasswordInput)
