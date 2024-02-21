year = int(input("Enter any year : \n"))
if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print ("Yes, It's a Leap Year!")
        else :
            print ("No, it's not a Leap Year!")
    else :
        print ("Yes, it's not a Leap Year!")
else :
    print ("No, it's not a Leap Year!")

