from django.contrib import admin
from userapp.models import User, Account, Address, FullName

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Address)
admin.site.register(FullName)
