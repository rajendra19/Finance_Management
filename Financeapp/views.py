
from django.shortcuts import render,redirect, get_object_or_404
from Financeapp.models import Expense
from Financeapp.forms import ExpenseModelForm
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from Financeapp.forms import LogInForm



def insert(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            try:
                form.save()

                return redirect('view_expense')
            except:
                pass
    form = LogInForm()
    return render(request, 'index.html', context={'form': form})


              # WE CAN DO THAT CRUD OPERATIONS USING DJANGO RESTFRAMEWORK ALSO.

# class ExpenseViewSet(viewsets.ModelViewSet):
#     serializer_class = ExpenseSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         if user.is_authenticated and user.userprofile.role == 'Admin':
#             return Expense.objects.all()
#         else:
#             return Expense.objects.filter(user=user)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
#
# class UserProfileViewSet(viewsets.ModelViewSet):
#     serializer_class = UserProfileSerializer
#     permission_classes = [permissions.IsAdminUser]
#
#     def get_queryset(self):
#         return UserProfile.objects.all()


def add_expense_form(request):
    if request.method == 'POST':
        form = ExpenseModelForm(request.POST)
        if form.is_valid():
            expense_request = form.save(commit=False)
            expense_request.created_by = request.user.id  # Member ID who created the request.So Assuming we have a User model with an 'id' field
            expense_request.save()
            return HttpResponse( 'Expense created successfully!')

        else:
            return HttpResponse( 'Expense create request failed.', status=400)
    else:
        form = ExpenseModelForm()

    return render(request, 'expense_form_modal.html', {'form': form})



@login_required
def view_expenses(request):
    if request.user.is_superuser:
        expenses = Expense.objects.all()
    else:
        expenses = Expense.objects.filter(user=request.user)

    return render(request, 'view_expenses.html', {'expenses': expenses})

@login_required
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if not request.user.is_superuser and expense.user != request.user:
        return redirect('view_expense')

    if request.method == 'POST':
        form = ExpenseModelForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('view_expense')

    form = ExpenseModelForm(instance=expense)
    return render(request, 'edit_expense.html', {'form': form, 'expense': expense})

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if not request.user.is_superuser and expense.user != request.user:
        return redirect('view_expense')

    if request.method == 'POST':
        expense.delete()
        return redirect('view_expense')

    return render(request, 'delete_expense.html', {'expense': expense})



def filter_expenses_by_name(request):
    search_name = request.GET.get('search_name')
    expenses = Expense.objects.all()

    if search_name:
        expenses = expenses.filter(name__icontains=search_name)

    return render(request, 'filter_expenses_by_name.html', {'expenses': expenses})


def filter_expenses_by_date(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    expenses = Expense.objects.all()

    if start_date:
        expenses = expenses.filter(date_of_expense__gte=start_date)
    if end_date:
        expenses = expenses.filter(date_of_expense__lte=end_date)

    return render(request, 'filter_expenses_by_date.html', {'expenses': expenses})
