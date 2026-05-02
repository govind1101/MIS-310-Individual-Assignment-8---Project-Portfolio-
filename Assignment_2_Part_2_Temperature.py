# Get input - Fahrenheit
temperature_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Processing - Convert to Celsius
temperature_celsius = (temperature_fahrenheit - 32) * 5/9

# Processing - Determine Water State
if temperature_celsius <= 0:
    status = "ice"
elif temperature_celsius <= 100:
    status = "Liquid"
else:
    status = "Gas"

# Output
print("Temperature(Celsius):", round(temperature_celsius, 1))
print("Water is:", status)
