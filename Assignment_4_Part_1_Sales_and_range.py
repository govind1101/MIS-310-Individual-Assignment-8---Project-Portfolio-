# List of sales for each day
Sale_list = [50, 75, 150, 125, 100]
# List of days of the week
Week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# Find the maximum sale
max_sale = max(Sale_list)
# Find the index of the maximum sale
max_index = Sale_list.index(max_sale)
# Find the corresponding day
max_day = Week_list[max_index]
# Display the results
print(f"The Max sales is ${max_sale}")
print(f"The Max sales day is {max_day}")