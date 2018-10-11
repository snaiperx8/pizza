from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from authenticate_app.forms import LoginForm, SignUpForm

def home(request):

	return render(request, 'home_temps/home.html', {})

def signup_view(request):
	signup_form = SignUpForm()

	if request.method == 'POST':
		signup_form = SignUpForm(request.POST)

		if signup_form.is_valid():
			user_obj = User.objects.create_user(
				username = signup_form.cleaned_data['username'],
				password = signup_form.cleaned_data['password'],
				email = signup_form.cleaned_data['email']
				)		
			user = user_obj.save()

			user_auth = authenticate(request,
			 username = signup_form.cleaned_data['username'],
			 password = signup_form.cleaned_data['password'])

			login(request, user_auth)
			return redirect(home)
	return render(request, 'auth_temps/signup.html', {'signup_form': signup_form})

def login_view(request):
	user_form = LoginForm()

	if request.method == 'POST':
		user_form = LoginForm(request.POST)

		if user_form.is_valid():
			user = authenticate(request,
			 username = user_form.cleaned_data['username'],
			 password = user_form.cleaned_data['password'])

			if user is not None:
				login(request, user)
				return redirect(home)
	return render(request, 'auth_temps/login.html', {'user_form':user_form})
	
def logout_view(request):
	logout(request)
	return redirect(home)
