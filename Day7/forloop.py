# Basic for loop syntax
# for variable in iterable:
#     # Code block to execute for each item
#     statement(s)

# ==============================================================

# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate over a string
word = "Python"
for letter in word:
    print(letter)

# Iterate over a range
for i in range(5):
    print(i)

#============================================================
# Iterating Over Different Data Types

# LIST
# Basic list iteration
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * 2)

# Output: 2, 4, 6, 8, 10

# List with mixed types
mixed = [1, "hello", 3.14, True]
for item in mixed:
    print(type(item))

# STRING
text = "Hello World"
for char in text:
    print(char.lower())


# TUPLES
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:  # Tuple unpacking
    print(f"X: {x}, Y: {y}")


# SETS
unique_numbers = {1, 2, 3, 4, 5}
for num in unique_numbers:
    print(num)  # Order is not guaranteed