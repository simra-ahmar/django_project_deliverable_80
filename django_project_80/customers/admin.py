from django.contrib import admin
from customers.models import Customers
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomersAdmin(UserAdmin):
	list_display = ('email', 'username', 'address', 'contact', 'date_joined', 'is_admin', 'is_staff', 'last_login')
	search_fields = ('email', 'username',)
	readonly_fields = ('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Customers, CustomersAdmin)