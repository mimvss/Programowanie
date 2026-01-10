# 12 - Most expensive category
categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_expense = max(expenses)
max_index = expenses.index(max_expense)
print(f"The most expensive category is {categories[max_index]} with {max_expense} units")
