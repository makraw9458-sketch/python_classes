# Accessing
fruits = ['apple', 'banana', 'cherry', 'abc']
# print(fruits[0])        # 'apple'
# print(fruits[-1])       # 'cherry'
# print(fruits[1:3])      # ['banana', 'cherry']

# Adding
fruits.append('orange')      # Adds to end
print(fruits)

# # fruits.insert(1, 'grape')    # Inserts at index
# # print(fruits)

# # fruits.extend(['mango', 'kiwi'])  # Adds multiple
# # print(fruits)

# # Removing
# # fruits.remove('banana')      # Removes first occurrence
# # print("remove: ",fruits)

# # popped = fruits.pop()        # Removes and returns last
# # print("pop: ",fruits)

# # popped_index = fruits.pop(0) # Removes at index
# # print("pop: ",fruits)

# # del fruits[0]                # Deletes at index
# # print("del: ",fruits)

# # fruits.clear()               # Empties list
# # print("clear: ",fruits)

# # Other
# # fruits = ['apple', 'banana', 'cherry']
# # print(fruits.index('banana'))       # Returns index: 1
# # print(fruits.count('apple'))        # Count occurrences

# # fruits.sort(reverse=True)
# # print(fruits)        

# # fruits.reverse()             # Reverses in place
# # print(fruits)
# sorted_list = sorted(fruits) # Returns new sorted list
# print(fruits)
# print(sorted_list)


# slicing
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# Get elements from index 2 to 4 (excludes 4)
print(fruits[2:5])  # ['cherry', 'date', 'elderberry']

# Get from start to index 3 (excludes 3)
print(fruits[:3])   # ['apple', 'banana', 'cherry']

# Get from index 2 to end
print(fruits[2:])   # ['cherry', 'date', 'elderberry', 'fig', 'grape']

# Get entire list (copy)
print(fruits[:])    # ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']


# with steps

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get every 2nd element
print(numbers[::2])   # [0, 2, 4, 6, 8]

# Get every 3rd element from index 1 to 8
print(numbers[1:8:3])  # [1, 4, 7]

# Get every 2nd element from index 2 to 8
print(numbers[2:8:2])  # [2, 4, 6]



# -ve idx
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Get last 2 elements
print(fruits[-2:])    # ['date', 'elderberry']

# Get elements from index -4 to -1 (excludes -1)
print(fruits[-4:-1])  # ['banana', 'cherry', 'date']

# Get from start to second last (excludes -1)
print(fruits[:-1])    # ['apple', 'banana', 'cherry', 'date']

# Get from 3rd last to last (excludes -1)
print(fruits[-3:-1])  # ['cherry', 'date']

# Everything except first and last
print(fruits[1:-1])   # ['banana', 'cherry', 'date']


# reverse
numbers = [0, 1, 2, 3, 4, 5]

# Reverse entire list
print(numbers[::-1])    # [5, 4, 3, 2, 1, 0]

# Reverse from index 1 to 4
print(numbers[4:1:-1])  # [4, 3, 2]

# Get reverse with step -2
print(numbers[::-2])    # [5, 3, 1]

# Get last 3 in reverse
print(numbers[:2:-1])   # [5, 4, 3]





numbers = [0, 1, 2, 3, 4, 5]

# With negative step, start > stop
print(numbers[5:2:-1])  # [5, 4, 3]
print(numbers[4:1:-2])  # [4, 2]

# Default with negative step goes from end to start
print(numbers[::-1])    # [5, 4, 3, 2, 1, 0]

# Can't go backward with start < stop
print(numbers[1:4:-1])  # [] (empty list)





















# ==================================================
# fruits.index(2, 'banana')    # insert at index
# print(fruits)