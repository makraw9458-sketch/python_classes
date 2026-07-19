## 4. **DICTIONARY** 📚

### Definition
Unordered collection of key-value pairs.

### Properties
- **Unordered**: No guaranteed order (though Python 3.7+ preserves insertion order)
- **Mutable**: Can be modified
- **Keys must be unique**: No duplicate keys
- **Keys must be hashable**: Immutable types only
- **Values can be any type**: Can be nested
- **Fast lookup**: O(1) average time complexity
- **Dynamic**: Can grow/shrink

### Syntax
```python
# Creation
my_dict = {'name': 'John', 'age': 30, 'city': 'NYC'}
mixed_dict = {'name': 'Alice', 1: 'one', (1,2): 'tuple_key'}
empty_dict = {}

# Using dict() constructor
dict_from_pairs = dict([('a', 1), ('b', 2)])
dict_from_kwargs = dict(name='Bob', age=25)
```

### Common Operations
```python
# Accessing
person = {'name': 'Alice', 'age': 30, 'city': 'London'}

# Get values
print(person['name'])          # 'Alice' (error if missing)
print(person.get('age'))       # 30 (returns None if missing)
print(person.get('country', 'UK'))  # Default value

# Adding/Updating
person['email'] = 'alice@email.com'  # Add new
person['age'] = 31                   # Update existing
person.update({'city': 'Paris', 'phone': '123'})

# Removing
del person['city']             # Remove key (error if missing)
popped = person.pop('age')     # Remove and return
popped_item = person.popitem() # Remove and return last item
person.clear()                 # Empty dict

# Iteration
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

for key in person.keys():      # Iterate keys
    print(key)

for value in person.values():  # Iterate values
    print(value)

# Other operations
len(person)                    # Number of items
'name' in person              # Check if key exists
list(person.keys())            # Get all keys
```

### Use Cases
- Storing structured data
- Configuration settings
- Caching (memoization)
- Counting occurrences (using collections.Counter)
- Database-like operations
- JSON data handling