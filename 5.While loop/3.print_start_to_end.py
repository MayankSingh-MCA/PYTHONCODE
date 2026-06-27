"""
start and end by user
start to end print using while loop
"""

start = int(input("Enter start number = "))

end = int(input("Enter end number = "))
"""
while start<=end:
    print(start, end=" ")
    start += 1

print(f"After while loop, start value is {start}")  # yaha par to start ki value hi(inputs ki value hi change ho gai) change ho gai , future code me problem ayega
"""
# to resolve this situation
i = start
while i <= end:
    print(i, end= " ")
    i += 1
print(f"After while loop, start value is {start}")
    

