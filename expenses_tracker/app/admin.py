from django.contrib import admin

# Register your models here.
from app.models import Expense, Profile

admin.site.register(Expense)
admin.site.register(Profile)