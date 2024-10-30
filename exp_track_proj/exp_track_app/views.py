from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
from datetime import timedelta
from django.utils import timezone


def index(request):
    expenses = Expense.objects.all().order_by("-date")
    expense_form = ExpenseForm()

    # Aggregate data for summaries
    total_expense = Expense.objects.aggregate(Sum("amount"))
    yearly_sum = Expense.objects.filter(
        date__gte=timezone.now() - timedelta(days=365)
    ).aggregate(Sum("amount"))
    monthly_sum = Expense.objects.filter(
        date__gte=timezone.now() - timedelta(days=30)
    ).aggregate(Sum("amount"))
    weekly_sum = Expense.objects.filter(
        date__gte=timezone.now() - timedelta(days=7)
    ).aggregate(Sum("amount"))
    daily_sums = (
        Expense.objects.filter(date__gte=timezone.now() - timedelta(days=30))
        .values("date")
        .annotate(sum=Sum("amount"))
        .order_by("-date")
    )
    category_sums = Expense.objects.values("category").annotate(sum=Sum("amount"))

    if request.method == "POST":
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
            return redirect("index")

    return render(
        request,
        "exp_track_app/index.html",
        {
            "expenses": expenses,
            "expense_form": expense_form,
            "total_expense": total_expense,
            "yearly_sum": yearly_sum,
            "monthly_sum": monthly_sum,
            "weekly_sum": weekly_sum,
            "daily_sums": daily_sums,
            "category_sums": category_sums,
        },
    )


def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    expense_form = ExpenseForm(request.POST or None, instance=expense)

    if request.method == "POST" and expense_form.is_valid():
        expense_form.save()
        return redirect("index")

    return render(request, "exp_track_app/edit.html", {"expense_form": expense_form})


def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == "POST":
        expense.delete()
        return redirect("index")
    return redirect("index")
