# 2. **TUPLE** 📦

### Definition
Ordered, immutable collection of items.

### Properties
- **Ordered**: Maintains insertion order
- **Immutable**: Cannot be modified after creation
- **Allow Duplicates**: Yes
- **Indexed**: Supports indexing and slicing
- **Heterogeneous**: Can hold different data types
- **Faster than lists**: More memory efficient

### Syntax
```python
# Creation
my_tuple = (1, 2, 3, 4, 5)
mixed_tuple = (1, "hello", 3.14, True)
single_tuple = (1,)           # Comma is necessary!
empty_tuple = ()

# Using tuple() constructor
tuple_from_list = tuple([1, 2, 3])

# Without parentheses (tuple packing)
coordinates = 10, 20, 30      # Also a tuple
```

### Common Operations
```python
# Accessing (same as lists)
t = ('a', 'b', 'c', 'd')
print(t[0])          # 'a'
print(t[-1])         # 'd'
print(t[1:3])        # ('b', 'c')

# Methods (limited due to immutability)
t.count('a')         # Count occurrences
t.index('b')         # Returns index

# Unpacking
a, b, c = (1, 2, 3)  # a=1, b=2, c=3
```

### Use Cases
- Fixed collections that shouldn't change
- Dictionary keys (lists can't be keys)
- Returning multiple values from functions
- Representing records/structures
- Better performance for read-only data

---
