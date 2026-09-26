# Assignment Operator (=)
field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110

# Arithmetic Operators (+, -, *, /)
total = field1 + field2 + field3 + field4 + field5
average = total/5

print("Total harvest :",total, "kg")
print("Average per field :",average,"kg")

# Total earnings
price_per_kg = 15
earnings = total * price_per_kg
print("Total earnings :",earnings,"Rs.")

# Floor division(//) and modulus (%)
bags = total//25
leftover = total % 25
print("Full bags packed  :",bags)
print("Leftover grain  :",leftover,"kg")

# Comparison
last_year = 500
print("Better than last year?", total > last_year)
print("Same as last year?", total == last_year)
print("At least as good?", total >= last_year)

# Assignment Operators
total += 30
print("After bonus crop  :",total,"kg")

total -= 15
print("After seed reserve  :",total,"kg")

# Final count
bags = total//25
print("Final bags packed  :",bags)

