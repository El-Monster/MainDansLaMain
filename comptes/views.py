from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpRequest, HttpResponse


def register(request: HttpRequest) -> HttpResponse:
	if request.method == 'POST':
		email = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('website_part:index')
		else:
			return render(request, 'website_part/contactez_nous.html')