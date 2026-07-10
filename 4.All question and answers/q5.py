# Sum of all the numbers from 1 to 100
'''
i = 1
total = 0
while i <= 100:
    total = total + i
    i += 1

print(f"Total = {total}")    '''

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

i = start

total = 0
while i <= end:
    total = total + i
    i += 1
print(f"Total = {total}")    