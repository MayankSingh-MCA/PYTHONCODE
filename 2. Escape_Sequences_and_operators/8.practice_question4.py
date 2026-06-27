"""
Q4: A student scored marks in three subjects. Take all three as input, calculate the total and average, and print both using an f-string.
"""

sub1 = int(input("Enter marks in sub1 ="))
sub2 = int(input("Enter marks in sub2 = "))
sub3 = int(input("Enter marks in sub3 = "))

total = sub1 + sub2 + sub3
average = total / 3
print(f"Total scored = {total} marks and average is {average}")
print(f"Total scored = {total} marks and average is {average:.3f}")
