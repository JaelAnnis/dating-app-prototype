from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.models import User
from .decorators import unauthenticated_user
from .models import *


# Create your views here.

def home(request):
	return render(request, 'UnMask/home.html')

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('match')
		else:
				messages.info(request, 'Username or password is incorrect.')
					

	context = {}
	return render(request, 'UnMask/login.html', context)


def registerPage(request):
		form = RegisterForm()

		if request.method == 'POST':
			form = RegisterForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')

				messages.success(request, 'Account was created for ' + username)

				return redirect('login')

		context = {"form" :form}
		return render(request, 'UnMask/register.html', context)

@login_required(login_url='login')
def matchPage(request):

	matches = Matches.objects.all()

	context = {"matches" :matches}
	return render(request, 'UnMask/match.html', context)


def profilePage(request):
	profile = request.user.profile
	form = ProfileForm(instance=profile)

	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES,instance=profile)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'UnMask/profile.html', context)

@login_required(login_url='login')
def chatPage(request):
	
	return render(request, 'UnMask/chat.html')


