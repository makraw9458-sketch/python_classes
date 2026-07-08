# Nested loops

# Multiplication table
for i in range(1, 40):
    for j in range(1, 40):
        print(f"{i} × {j} = {i*j}")
    print("-" * 50)


# Matrix iteration
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=",")
    print()