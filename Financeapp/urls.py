
from django.urls import path
from Financeapp import views


urlpatterns = [

    path('',views.insert),
    path('add_expense/',views.add_expense_form,name='add_expense'),
    path('view_expense/', views.view_expenses, name='view_expense'),
    path('expenses/<int:expense_id>/edit/', views.edit_expense, name='edit_expense'),
    path('expenses/<int:expense_id>/delete/', views.delete_expense, name='delete_expense'),
    path('filter_by_name/',views.filter_expenses_by_name,name='filter_by_name'),
    path('filter_by_date/',views.filter_expenses_by_date,name='filter_by_date'),

]
