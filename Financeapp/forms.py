
from django import forms
from Financeapp.models import Expense, login_user



class ExpenseModelForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['user_name','date_of_expense','category','description','amount']



class LogInForm(forms.ModelForm):
    class Meta:
        model = login_user
        fields ='__all__'
        widgets = {
            'email':
                forms.EmailInput(attrs={'class': 'form-control'}),
            'password':
                forms.TextInput(attrs={'class': 'form-control'}),
        }
