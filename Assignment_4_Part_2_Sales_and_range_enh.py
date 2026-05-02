# Create empty list to store numbers
numbers = []
# Prompt the user for the first number
value = float(input("Enter value: "))
# Continue accepting numbers until the user enters 0
while value != 0:
    numbers.append(value)
    value = float(input("Enter value (or 0 to end): "))
# Display the list of numbers entered
print(numbers)
# Ensure the list is not empty calculate Range
if len(numbers) > 0:
    highest = max(numbers)
    lowest = min(numbers)
    range_value = highest - lowest
# Display the range 
    print(f"Range= {range_value}")
else:
    print("No numbers were entered.")