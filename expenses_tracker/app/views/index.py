from django.shortcuts import render, redirect

from app.common.calculate import calculate_budget_left
from app.common.profile import get_profile
from app.forms.profile import ProfileForm
from app.models import Profile, Expense
from app.views.profiles import create_profile


def index(request):
    if Profile.objects.exists():
        profile = get_profile()
        # expenses = Expense.objects.all()
        expenses = profile.expense_set.all()

        profile.budget_left = calculate_budget_left(profile, expenses)

        # sum_costs = sum([expense.price for expense in expenses])
        # profile.budget_left = profile.budget - sum_costs

        context = {
            'profile': profile,
            'expenses': expenses,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        return create_profile(request)