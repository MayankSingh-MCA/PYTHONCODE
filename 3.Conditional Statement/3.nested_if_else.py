# Age >= 18
# Certificate -> True

age = int(input("Enter your age = "))
certificate = True

if age >= 18 and age <= 45:
    if certificate == True:
        print("You will be hired")
    else:
        print("Cannot hire due to no certificate")
else:
    print("Cannot hire, age is less than 18 or greater than 45")
