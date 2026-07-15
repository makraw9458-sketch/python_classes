n = int(input("Enter a number: "))
count = 0

for i in range(2, n+1, 2):
    print(i , end=", ")
    count += 1

print("\nCount: ", count)