'''
admin site model registration
'''
from django.contrib import admin
from my_app.models import Customer, UserProfileInfo

# Register your models here.
admin.site.register(Customer)
admin.site.register(UserProfileInfo)
