num1 = input("Enter number 1 =")
num2 = input("Enter number 2 =")

total = num1 + num2
print(f"Total = {total}")

"""output
Enter number 1 =12qw 
Enter number 2 =12er 
Total = 12qw12er
"""

num3 = int(input("Enter number 3 ="))

num4 = int(input("Enter number 4 ="))

total = num3 + num4
print(f"Total is = {total}")

"""
Enter number 1 =12
Enter number 2 =12
Total = 1212  # This is because input by default string leta hai. 12 ko string consider krke add ar diya 1212
Enter number 3 =12
Enter number 4 =12
Total is = 24  # Yaha par input ko pahle hi integer kr diya hai isliye output 24 aya
"""