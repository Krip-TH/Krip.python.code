# Personal Finance Calculator
# Student: [Your Name]
# Date: 2025-07-25
# Purpose: Calculate monthly budget and savings
name = input("what is your name :")
date = input("Today's date is (DD/MM/YYYY):")

# -- Input Section --
monthly_income = float(input(" monthly income (THB): "))
rent_cost = float(input(" monthly rent/housing cost (THB): "))
transportation_cost = float(input(" monthly transportation cost (THB): "))
food_budget = int(input(" monthly food budget (THB): "))
entertainment_budget = int(input(" monthly entertainment budget (THB): "))
emergency_fund_percent = float(input(" percentage to save for emergency (e.g., 10.5): "))
investment_percent = float(input(" percentage to invest (e.g., 15.0): "))

# -- Calculation --
total_fixed_expenses = rent_cost + transportation_cost
total_variable_expenses = food_budget + entertainment_budget
total_expenses = total_fixed_expenses + total_variable_expenses
remaining_income = monthly_income - total_expenses
emergency_fund_amount = monthly_income * (emergency_fund_percent / 100)
investment_amount = monthly_income * (investment_percent / 100)
available_for_savings = remaining_income - emergency_fund_amount - investment_amount
expense_ratio = (total_expenses / monthly_income) * 100

# -- Personal Details --
print("\n=== PERSONAL DETAILS ===")
print(f"Student : {name}")
print(f"Date : {date}")

# -- Output --
print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {total_fixed_expenses:.2f} THB")
print(f"Variable Expenses: {total_variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent:.0f}%): {emergency_fund_amount:.2f} THB")
print(f"Investment ({investment_percent:.0f}%): {investment_amount:.2f} THB")
print(f"Available for Savings: {available_for_savings:.2f} THB")

print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")