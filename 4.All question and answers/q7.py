"""
Ask a number from the user, print the multiplication table upto 10

Enter a number = 4

4 x 1 = 4
4 x 2 = 8
...
...
...

4 x 9 = 36
4 x 10 = 40




"""
num = int(input("Enter a number = "))

i = 1
while i <= 10:
    print(f"{num} x {i} = {num*i}")

    i += 1

