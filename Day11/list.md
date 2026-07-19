# 1. **LIST** 📋

### Definition
Ordered, mutable (changeable) collection of items.

### Properties
- **Ordered**: Maintains insertion order
- **Mutable**: Can be modified after creation
- **Allow Duplicates**: Yes
- **Indexed**: Supports indexing and slicing
- **Heterogeneous**: Can hold different data types
- **Dynamic**: Can grow/shrink in size

### Syntax
```python
# Creation
my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
empty_list = []

# Using list() constructor
list_from_tuple = list((1, 2, 3))
```

### Common Operations
```python
# Accessing
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])        # 'apple'
print(fruits[-1])       # 'cherry'
print(fruits[1:3])      # ['banana', 'cherry']

# Adding
fruits.append('orange')      # Adds to end
fruits.insert(1, 'grape')    # Inserts at index
fruits.extend(['mango', 'kiwi'])  # Adds multiple

# Removing
fruits.remove('banana')      # Removes first occurrence
popped = fruits.pop()        # Removes and returns last
popped = fruits.pop(idx)        # Removes  with index
popped_index = fruits.pop(0) # Removes at index
del fruits[0]                # Deletes at index
fruits.clear()               # Empties list

# Other
fruits = ['apple', 'banana', 'cherry']
fruits.index('banana')       # Returns index: 1
fruits.index(2, 'banana')    # insert at index
fruits.count('apple')        # Count occurrences
fruits.sort()                # Sorts in place
fruits.reverse()             # Reverses in place
sorted_list = sorted(fruits) # Returns new sorted list
```

### Use Cases
- Storing ordered collections
- When you need to modify data frequently
- Implementing stacks (LIFO) and queues (FIFO)
- Keeping track of items in order

---


# Complete Guide to List Slicing in Python 🎯

List slicing is one of Python's most powerful and elegant features. It allows you to extract, modify, and manipulate portions of lists with simple, readable syntax.

---

## 📖 Basic Syntax

```python
list[start:stop:step]
```

- **start** (optional): Index to begin slicing (inclusive) - defaults to 0
- **stop** (optional): Index to end slicing (exclusive) - defaults to end of list
- **step** (optional): Increment between items - defaults to 1

---

## 🎯 Basic Slicing

### Simple Slice
```python
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# Get elements from index 2 to 4 (excludes 4)
print(fruits[2:5])  # ['cherry', 'date', 'elderberry']

# Get from start to index 3 (excludes 3)
print(fruits[:3])   # ['apple', 'banana', 'cherry']

# Get from index 2 to end
print(fruits[2:])   # ['cherry', 'date', 'elderberry', 'fig', 'grape']

# Get entire list (copy)
print(fruits[:])    # ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
```

### With Step Parameter
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get every 2nd element
print(numbers[::2])   # [0, 2, 4, 6, 8]

# Get every 3rd element from index 1 to 8
print(numbers[1:8:3])  # [1, 4, 7]

# Get every 2nd element from index 2 to 8
print(numbers[2:8:2])  # [2, 4, 6]
```

---

## 🔢 Negative Indexing

Negative indices count from the end of the list (-1 is the last element).

```python
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
```

---

## 🔄 Reverse Slicing

### Using Negative Step
```python
numbers = [0, 1, 2, 3, 4, 5]

# Reverse entire list
print(numbers[::-1])    # [5, 4, 3, 2, 1, 0]

# Reverse from index 1 to 4
print(numbers[4:1:-1])  # [4, 3, 2]

# Get reverse with step -2
print(numbers[::-2])    # [5, 3, 1]

# Get last 3 in reverse
print(numbers[:2:-1])   # [5, 4, 3]
```

### Important: Negative Step Rules
```python
numbers = [0, 1, 2, 3, 4, 5]

# With negative step, start > stop
print(numbers[5:2:-1])  # [5, 4, 3]
print(numbers[4:1:-2])  # [4, 2]

# Default with negative step goes from end to start
print(numbers[::-1])    # [5, 4, 3, 2, 1, 0]

# Can't go backward with start < stop
print(numbers[1:4:-1])  # [] (empty list)
```

---

## ✏️ Modifying Lists with Slicing

### Assigning to Slices
```python
numbers = [0, 1, 2, 3, 4, 5]

# Replace slice
numbers[1:4] = [10, 20, 30]
print(numbers)  # [0, 10, 20, 30, 4, 5]

# Replace with different length
numbers[1:3] = [100, 200, 300, 400]
print(numbers)  # [0, 100, 200, 300, 400, 30, 4, 5]

# Insert using slice
numbers[2:2] = [99, 98]  # Insert at index 2
print(numbers)  # [0, 100, 99, 98, 200, 300, 400, 30, 4, 5]

# Delete using slice
numbers[1:4] = []
print(numbers)  # [0, 200, 300, 400, 30, 4, 5]

# Replace with empty list (delete)
numbers[2:5] = []
print(numbers)  # [0, 200, 4, 5]
```

### Using Step in Assignment
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Replace every 2nd element
numbers[::2] = [10, 20, 30, 40, 50]
print(numbers)  # [10, 1, 20, 3, 30, 5, 40, 7, 50, 9]

# Must match length when using step
# numbers[::2] = [1, 2]  # ValueError: attempt to assign sequence of size 2 to extended slice of size 5
```

---

## 📝 Advanced Slicing Patterns

### Common Patterns
```python
data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Get first element
first = data[:1]     # ['a'] (as list)
first = data[0]      # 'a'   (as element)

# Get last element
last = data[-1:]     # ['h'] (as list)
last = data[-1]      # 'h'   (as element)

# Get all except first
rest = data[1:]      # ['b', 'c', 'd', 'e', 'f', 'g', 'h']

# Get all except last
all_but_last = data[:-1]  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Get middle elements (excluding first and last)
middle = data[1:-1]  # ['b', 'c', 'd', 'e', 'f', 'g']

# Get every even index
evens = data[::2]    # ['a', 'c', 'e', 'g']

# Get every odd index
odds = data[1::2]    # ['b', 'd', 'f', 'h']

# Get last 3
last_three = data[-3:]  # ['f', 'g', 'h']

# Get first 3
first_three = data[:3]  # ['a', 'b', 'c']

# Get every 2nd from index 2 to 6
subset = data[2:6:2]  # ['c', 'e']
```

### Slicing in Loops
```python
# Processing in chunks
numbers = list(range(20))
chunk_size = 5

for i in range(0, len(numbers), chunk_size):
    chunk = numbers[i:i + chunk_size]
    print(chunk)

# Output:
# [0, 1, 2, 3, 4]
# [5, 6, 7, 8, 9]
# [10, 11, 12, 13, 14]
# [15, 16, 17, 18, 19]
```

---

## 🧠 Slicing vs Other Methods

### Slicing vs Copying
```python
original = [1, 2, 3, 4]

# Different ways to copy
shallow_copy1 = original[:]      # Slicing
shallow_copy2 = original.copy()  # copy() method
shallow_copy3 = list(original)   # Constructor

# They all create independent copies
original[0] = 99
print(original)     # [99, 2, 3, 4]
print(shallow_copy1)  # [1, 2, 3, 4]

# But note: still shallow for nested lists
nested = [[1, 2], [3, 4]]
copy = nested[:]
copy[0][0] = 99
print(nested)  # [[99, 2], [3, 4]] - Original affected!
```

### Slicing vs Loops
```python
# Instead of loop for extracting first 3
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# Manual loop (verbose)
result = []
for i in range(3):
    result.append(names[i])

# Slicing (elegant)
result = names[:3]  # ['Alice', 'Bob', 'Charlie']

# Finding every other element
# Manual (verbose)
result = []
for i in range(0, len(names), 2):
    result.append(names[i])

# Slicing (elegant)
result = names[::2]  # ['Alice', 'Charlie', 'Eve']
```

---

## 💡 Pro Tips & Tricks

### 1. Shallow Copy
```python
# Quick copy of a list
original = [1, 2, 3]
copy = original[:]
copy.append(4)
print(original)  # [1, 2, 3]
print(copy)      # [1, 2, 3, 4]
```

### 2. Remove First/Last Elements
```python
items = ['a', 'b', 'c', 'd', 'e']

# Remove first
items = items[1:]  # ['b', 'c', 'd', 'e']

# Remove last
items = items[:-1]  # ['a', 'b', 'c', 'd']
```

### 3. Palindrome Check
```python
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("radar"))    # True
print(is_palindrome("python"))   # False
```

### 4. Rotate List
```python
def rotate_left(lst, n):
    return lst[n:] + lst[:n]

def rotate_right(lst, n):
    return lst[-n:] + lst[:-n]

numbers = [1, 2, 3, 4, 5]
print(rotate_left(numbers, 2))   # [3, 4, 5, 1, 2]
print(rotate_right(numbers, 2))  # [4, 5, 1, 2, 3]
```

### 5. Getting Last N Items
```python
def last_n(lst, n):
    return lst[-n:] if n > 0 else []

numbers = [1, 2, 3, 4, 5]
print(last_n(numbers, 3))  # [3, 4, 5]
```

---

## 🚨 Common Pitfalls

### 1. Empty Slices
```python
numbers = [1, 2, 3, 4, 5]

# Start > Stop returns empty list
print(numbers[4:2])  # []

# Start out of bounds
print(numbers[10:15])  # []

# End out of bounds (handled gracefully)
print(numbers[2:10])  # [3, 4, 5]
```

### 2. Step Must Not Be Zero
```python
# This will raise ValueError
# numbers[::0]  # ValueError: slice step cannot be zero
```

### 3. Negative Step Confusion
```python
numbers = [0, 1, 2, 3, 4, 5]

# This might be confusing
print(numbers[-2:-5:-1])  # [4, 3, 2]
# Think: start at -2 (4), go backward to -5 (exclude), step -1
```

### 4. Modifying While Iterating
```python
# Bad practice - modifying list while iterating
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = 0

# Better using slicing
numbers = [1, 2, 3, 4, 5]
numbers[1::2] = [0, 0]  # [1, 0, 3, 0, 5]
```

---

## 🎯 Quick Reference Card

| Slice | Description | Example (lst = [0,1,2,3,4,5]) |
|-------|-------------|-------------------------------|
| `lst[:]` | Copy entire list | `[0,1,2,3,4,5]` |
| `lst[n:]` | From n to end | `lst[2:]` → `[2,3,4,5]` |
| `lst[:n]` | From start to n-1 | `lst[:3]` → `[0,1,2]` |
| `lst[n:m]` | From n to m-1 | `lst[2:4]` → `[2,3]` |
| `lst[-n:]` | Last n elements | `lst[-2:]` → `[4,5]` |
| `lst[:-n]` | All except last n | `lst[:-2]` → `[0,1,2,3]` |
| `lst[n:m:k]` | n to m-1 step k | `lst[1:5:2]` → `[1,3]` |
| `lst[::-1]` | Reverse list | `[5,4,3,2,1,0]` |
| `lst[n::-1]` | From n to start backwards | `lst[3::-1]` → `[3,2,1,0]` |
| `lst[:n:-1]` | From end to n+1 backwards | `lst[:2:-1]` → `[5,4,3]` |
| `lst[::k]` | Every kth element | `lst[::2]` → `[0,2,4]` |
| `lst[n::k]` | Every kth from n | `lst[1::2]` → `[1,3,5]` |

---

## 🧪 Practice Exercises

### Exercise 1: Extract Subsets
```python
# Given this list, use slicing to extract:
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 1. Get first 4 elements
# 2. Get last 3 elements
# 3. Get elements from index 2 to 6
# 4. Get every 2nd element
# 5. Get every 3rd element from index 1 to 8
# 6. Get all except first and last
# 7. Reverse the list
# 8. Get elements at even indices only

# Solutions:
print(numbers[:4])       # [10, 20, 30, 40]
print(numbers[-3:])      # [80, 90, 100]
print(numbers[2:7])      # [30, 40, 50, 60, 70]
print(numbers[::2])      # [10, 30, 50, 70, 90]
print(numbers[1:8:3])    # [20, 50, 80]
print(numbers[1:-1])     # [20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[::-1])     # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
print(numbers[::2])      # [10, 30, 50, 70, 90]
```

### Exercise 2: Replace Subsets
```python
# Given this list, use slicing to:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 1. Replace 'c', 'd', 'e' with 'X', 'Y', 'Z'
# 2. Insert 'M', 'N', 'O' at index 3
# 3. Delete 'b', 'c'
# 4. Replace every 2nd element with '*'

# Solutions:
letters[2:5] = ['X', 'Y', 'Z']    # ['a', 'b', 'X', 'Y', 'Z', 'f', 'g']
letters[3:3] = ['M', 'N', 'O']    # ['a', 'b', 'X', 'M', 'N', 'O', 'Y', 'Z', 'f', 'g']
letters[1:3] = []                 # ['a', 'M', 'N', 'O', 'Y', 'Z', 'f', 'g']
letters[::2] = ['*'] * 4          # ['*', 'M', '*', 'O', '*', 'Z', '*']
```

---

## 🔥 Advanced: Custom Slicing Class

```python
class Sliceable:
    def __init__(self, data):
        self.data = data
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            # Custom slice behavior
            return [self.data[i] for i in range(key.start or 0, 
                                                key.stop or len(self.data), 
                                                key.step or 1)]
        return self.data[key]

# Usage
obj = Sliceable([1, 2, 3, 4, 5])
print(obj[1:4])    # [2, 3, 4]
print(obj[::2])    # [1, 3, 5]
```

---

Remember: **Slicing doesn't modify the original list** (unless you use assignment). Always create a new copy when you need to preserve the original data! 🎯