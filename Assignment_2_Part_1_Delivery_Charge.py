# Get Inputs
packages = int(input("Enter the number of packages: "))
shipping_type = input("Enter Shipping type (standard/express): ")

# Processing - determine rate
if shipping_type == "standard":
    rate = 10
elif shipping_type == "express":
    rate = 15
else:
    rate = 0

# Calculation - delivery charge
delivery_charge = packages * rate

# Output
print("Total charge  ${:,.2f}".format(delivery_charge))