from django.contrib import admin
from .models import Account
# Register your models here.
class AccountAdmin(admin.ModelAdmin):
  list_display = ('email', 'first_name', 'last_name', 'username', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_staff', 'is_superuser')
  list_display_links =( 'email', 'first_name', 'last_name')

  filter_horizontal = ()
  list_filter = ()
  fieldsets = ()
  ordering = ('-date_joined',)




admin.site.register(Account, AccountAdmin)