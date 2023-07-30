from django.db import models
from django.contrib.auth.models import User



class login_user(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Health', 'Health'),
        ('Electronics', 'Electronics'),
        ('Travel', 'Travel'),
        ('Education', 'Education'),
        ('Books', 'Books'),
        ('Others', 'Others'),
    ]

    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_expense = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES,default=None)
    description = models.TextField()
    amount = models.PositiveIntegerField(default=1)
    created_by = models.IntegerField()  # Assuming this is the Member ID
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Member', 'Member'),
    ]
    user = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True,blank=True, null=True)
    password = models.CharField(max_length=128,blank=True,null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')



