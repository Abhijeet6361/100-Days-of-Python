print("Welcome to Python Pizza")
print("How big of a Pizza would you like?\n We offer:\n Small Pizza (S) : $15 \n Medium Pizza (M) : $20 \n Large Pizza (L) : $25")
pizza = input("Enter the size of your pizza [ S , M or L ] : \n")
print("Would You Like to add Pepperoni?\n $2 for Small Pizza\n $3 for Medium & Large Pizza\n ")
Pepperoni = input("Pepperoni Yes / No? \n")
print("Would You Like to add extra Cheese? \n $1 for any Pizza")
Cheese = input("Extra Cheese Yes / No? \n")
price = 0
if pizza == "S" :
    price += 15
    if Pepperoni == "Yes" :
        price += 2
        if Cheese == "Yes" : 
            price += 1
elif pizza == "M" :
    price += 20
    if Pepperoni == "Yes" :
        price += 3
        if Cheese == "Yes" : 
            price += 1
elif pizza == "L" :
    price += 25
    if Pepperoni == "Yes" :
        price += 3
        if Cheese == "Yes" : 
            price += 1
else :
    print("Please Give only S, M, or L")
print(f"Your Total is ${price}")