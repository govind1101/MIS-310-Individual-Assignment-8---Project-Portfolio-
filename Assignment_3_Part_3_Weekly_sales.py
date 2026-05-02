# Problem 1: Weekly Sales Tracker
# Part a: Track sales over 5 days

# Prompt user for total sales target
total_target = float(input("Enter total sales target: "))
cumulative_sales = 0.0

# Loop over 5 days
for day in range(1,6):
    sales = float(input(f"Enter day {day} sales: "))
    cumulative_sales += sales
    percentage = (cumulative_sales/total_target) * 100
    print(f"Cumulative Sales: {cumulative_sales:.1f} ({percentage:.1f} %)\n")