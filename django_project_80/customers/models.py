from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyCustomersManager(BaseUserManager):
	def create_user(self, email, username, address, contact, password=None ):
		if not email:
			raise ValueError("Customers must have an email address")
		if not username:
			raise ValueError("Customers must have a username")
		if not address:
			raise ValueError("Customers must have an address")
		if not contact:
			raise ValueError("Customers must have a contact")

		user = self.model(
				email = self.normalize_email(email),
				username = username,
				address = address,
				contact = contact
			)

		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_superuser(self, email, username, address, contact, password=None ):
		user = self.create_user(
				email = self.normalize_email(email),
				username = username,
				address = address,
				contact = contact,
				password = password
			)
		user.is_staff = True
		user.is_admin = True
		user.is_active = True
		user.is_superuser = True

		user.save(using = self._db) 
		return user



class Customers(AbstractBaseUser):
	email = models.EmailField(verbose_name = "email", max_length = 60, unique = True)
	username = models.CharField(max_length = 30, unique = True)
	date_joined = models.DateTimeField(verbose_name = 'date joined', auto_now_add = True)
	last_login = models.DateTimeField(verbose_name = 'last login', auto_now = True)
	is_admin = models.BooleanField(default = False)
	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)
	is_superuser = models.BooleanField(default = False)

	
	address = models.CharField(max_length = 69, unique = False)
	contact = models.IntegerField(unique = True)
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [ 'username', 'address', 'contact',]

	objects = MyCustomersManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj = None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True




