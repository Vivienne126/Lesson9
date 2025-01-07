print("What do you want")
print("1.car")
print("2.Bike")
choice=int(input("Enter your choice"))

if choice==1:
    print("Choose which car you want")
    print("1.sedan")
    print("2.xuv")
    choice2=int(input("Enter your choice"))
    if choice2==1:
        print("You have chosen sedan")
    else:
        print("You have chosen xuv")

elif choice==2:
    print("Choose which bike you want")
    print("1.scootie")
    print("2.scooter")
    choice3=int(input("Enter your choice"))
    if choice3==1:
        print("You have chosen scootie")
    else:
        print("You have chosen scooter")
else:
    print("Invalid input")
    