## 3. **SET** 🎯

### Definition
Unordered collection of unique elements.

### Properties
- **Unordered**: No index or order guarantee
- **Mutable**: Can add/remove elements
- **No Duplicates**: Automatically removes duplicates
- **Heterogeneous**: Can hold different data types
- **Hashable elements**: Elements must be hashable
- **Mathematical operations**: Supports set operations

### Syntax
```python
# Creation
my_set = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14}  # Must be hashable
empty_set = set()               # Not {} (that's empty dict)

# From other collections
set_from_list = set([1, 2, 2, 3])  # {1, 2, 3}
```

### Common Operations
```python
# Basic operations
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# Adding/Removing
s1.add(6)                 # Adds element
s1.update([7, 8, 9])      # Adds multiple
s1.remove(5)              # Removes (error if missing)
s1.discard(10)            # Removes (no error if missing)
popped = s1.pop()         # Removes random element
s1.clear()                # Empties set

# Set operations
union = s1 | s2           # OR: {1,2,3,4,5,6,7,8}
intersection = s1 & s2    # AND: {4,5}
difference = s1 - s2      # IN s1 NOT in s2: {1,2,3}
symmetric_diff = s1 ^ s2  # XOR: {1,2,3,6,7,8}

# Comparison
s1.issubset(s2)           # Check if subset
s1.issuperset(s2)         # Check if superset
s1.isdisjoint(s2)         # Check if no common elements
```

### Use Cases
- Removing duplicates from collections
- Membership testing (faster than lists)
- Mathematical operations (union, intersection)
- Tracking unique items
- Finding commonalities/differences between collections
