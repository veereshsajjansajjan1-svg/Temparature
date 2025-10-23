temp = float(input("Enter temperature in °C: "))

if temp < 20:
    status = "Cold"
elif temp <= 30:
    status = "Normal"
else:
    status = "Hot"

print(f"Temperature: {temp}°C")
print("Status:", status)

temp = float(input("Enter temperature in °C: "))

if temp < 20:
    status = "Cold"
elif temp <= 30:
    status = "Normal"
else:
    status = "Hot"

fahrenheit = (temp * 9/5) + 32

print(f"Temperature: {temp}°C")
print("Status:", status)
print(f"Temperature in Fahrenheit: {fahrenheit}°F")
