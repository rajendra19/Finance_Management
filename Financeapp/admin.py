from django.contrib import admin
from Financeapp.models import Expense,UserProfile

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['id','user_name','date_of_expense','category','description','amount','created_by','created_at','updated_at']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id','email','password','role']
