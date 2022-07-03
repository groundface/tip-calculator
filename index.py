bill = float(input("How much is the total bill? "))

tip = int(input("How much would you like to tip? 10, 12, or 15"))

people = int(input("How many people will be splitting the bill? "))

result = (bill * (1 + tip / 100)) / people

print(f"Each person shonuld pay: {round(result, 2)}")
