def calculate_budget_left(profile, expenses):
    sum_costs = sum([expense.price for expense in expenses])
    budget_left = profile.budget - sum_costs

    return budget_left
