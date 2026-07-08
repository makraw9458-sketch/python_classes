# The Range Function
# The range() function generates a sequence of numbers, commonly used in for loops for iteration control.

# syntax
# range(stop)                 # 0 to stop-1
# range(start, stop)          # start to stop-1
# range(start, stop, step)    # start to stop-1 with step size

# =======================================================


# Basic range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Range with start and stop
for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

# Range with step
for i in range(10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Reverse range
for i in range(10, -10, -1):
    print(i)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# Using range with len()
items = ["a", "b", "c", "d"]
for i in range(len(items)):
    print(f"Index {i}: {items[i]}")