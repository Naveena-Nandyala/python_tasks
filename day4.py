# Assignment: current bill 0 to 100 - per unit 50 rupees ex: 30 units => 30 * 50 = 1500
# 101 to 200 - 100 rupees per unit
#  more than 200 - 150 rupees per unit
#  with and without elif

# Without elif statement:

units = int(input("Enter the Units"))
if units >= 0 and units <= 100:
    print("Total Current Bill for" , units, "units:", (units * 50))
if units >= 101 and units <= 200:
    print("Total Current Bill for" , units, "units :", (units * 100))
if units > 200:
    print("Total Current Bill for" , units, "units :", (units * 150))

# With elif statement: 

unit = int(input("Enter the Units"))
if unit >= 0 and unit <= 100:
    print("Total Current Bill for", unit, "units :", (unit * 50))
elif unit >= 101 and unit <= 200:
    print("Total Current Bill for", unit, "units :", (unit * 100))
elif unit > 200:
    print("Total Current Bill for", unit, "units :", (unit * 150))
else:
    print("Invalid details")