from django import forms
from django.contrib.auth.forms import User

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 30, required = True)
	password = forms.CharField(widget = forms.PasswordInput)

class SignUpForm(forms.ModelForm):
	username = forms.CharField(max_length = 30, required = True)
	password = forms.CharField(widget = forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username', 'password', 'email')