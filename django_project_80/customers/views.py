from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from customers.forms import RegistrationForm, CustomersAuthenticationForm


# Create your views here.

def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			customers = form.save()
			login(request, customers)
			return redirect('blog-home')
		else:
			context['registration_form'] = form
	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'customers/register.html', context)




def logout_view(request):
	logout(request)
	return redirect('blog-home')

def login_view(request):
	context = {}

	user = request.user
	if user.is_authenticated:
		return redirect('blog-home')

	if request.POST:
		form = CustomersAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email = email, password = password)

			if user:
				login(request, user)
				return redirect("blog-home")


	else:
		form = CustomersAuthenticationForm()

	context['login_form'] = form
	return render(request, 'customers/login.html', context)


