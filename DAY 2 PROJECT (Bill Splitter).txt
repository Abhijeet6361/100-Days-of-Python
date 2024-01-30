print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give? 10,12, or 15?\n"))
split = int(input("How many people to split the bill?\n"))
pay = ((tip/100)*(bill) + bill) / split
print(f"Each person should pay {pay}")