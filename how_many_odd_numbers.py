count=0

for i in range(10):
    odd=int(input(f"Enter number {i+1}: "))
    if odd % 2 != 0:
        count += 1

print("There are",count, " odd numbers.")
