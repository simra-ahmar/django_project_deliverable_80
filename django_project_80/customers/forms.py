from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from customers.models import Customers


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length = 69, help_text = 'Required, add a valid email address')
	address = forms.CharField(max_length = 69, help_text = 'Required, add a valid address')
	contact = forms.IntegerField(help_text = 'Required, add a valid phone number')

	class Meta:
		model = Customers
		fields = ("email", "username", "password1", "password2", "address", "contact")



class CustomersAuthenticationForm(forms.ModelForm):
	password = forms.CharField(label = 'password', widget = forms.PasswordInput)

	class Meta:
		model = Customers
		fields = ('email', 'password')

	def clean(self):
		email = self.cleaned_data['email']
		password = self.cleaned_data['password']
		if not authenticate(email = email, password = password):
			raise forms.ValidationError("Invalid LOGIN LOLOLOL")