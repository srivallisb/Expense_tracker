from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail


def signup(request):
	if request.method=="POST":
		username =request.POST["username"]
		password = request.POST["password"]
		email = request.POST["email"]

		user = User.objects.create_user(
				username = username,
				password =password,
				email=email
			)
		login(request,user)
		subject = 'welcome to expense tracker app'
		message = f'Hi {user.username}, use this expense tracker application to track your daily expenses.'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [user.email,]
		send_mail( subject, message, email_from, recipient_list )
		return redirect("/dashboard/")
	return render(request, "signup.html")


def signin(request):
	if request.method=="POST":
		username =request.POST["username"]
		password = request.POST["password"]

		user = authenticate(request, username=username, password=password)

		if user != None:

			login(request,user)
			return redirect("/dashboard/")
		else:

			return redirect("/signup/")
	return render(request, "signin.html")

def signout(request):
	logout(request)

	return redirect("/signin/")


