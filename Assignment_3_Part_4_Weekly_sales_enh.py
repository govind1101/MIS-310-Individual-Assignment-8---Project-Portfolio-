# Problem 1: Weekly Sales Tracker
# Part b: Track sales over 5 days with input validation

#Prompt user for total sales target
while True:
    try:
        total_target = float(input("Enter total sales target: "))
        if total_target <= 0:
            print("Sales target must be greater than 0. Try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Enter a numeric value.")

cumulative_sales = 0.0 # Initializing Cumulative Sales

# Loop over 5 days with input validation
for day in range(1,6):
    while True:
        try:
            sales = float(input(f"Enter day {day} sales: "))
            if sales <= 0:
                print("Sales must be greater than 0. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Enter a numeric value.")
    cumulative_sales += sales
    percentage = (cumulative_sales/total_target) * 100
    print(f"Cumulative Sales: {cumulative_sales:.1f} ({percentage:.1f} %)\n")
