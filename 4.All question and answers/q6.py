# Sum of all the numbers from 1 to 100 divisible by 2 and 7.

start = int(input("Enter start number = "))

end = int(input("Enter end number = "))

i = start
total = 0

while i <= end:
    if i % 2 == 0 and i % 7 == 0:
        total = total + i
    i += 1
print(f"Total = {total}") 
      