## Advanced Examples 🚀

### Nested Structures
```python
# List of dictionaries
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

# Dictionary of lists
grades = {
    'math': [85, 92, 78],
    'science': [90, 88, 95],
    'english': [75, 80, 85]
}

# Set of tuples (for unique pairs)
coordinates = {(1, 2), (3, 4), (1, 2)}  # Becomes {(1,2), (3,4)}
```

### Type Conversion
```python
# List ↔ Tuple
list_to_tuple = tuple([1, 2, 3])
tuple_to_list = list((1, 2, 3))

# List ↔ Set (removes duplicates)
list_to_set = set([1, 2, 2, 3])     # {1, 2, 3}
set_to_list = list({1, 2, 3})       # [1, 2, 3]

# Dictionary ↔ List of tuples
dict_to_tuples = list({'a': 1, 'b': 2}.items())  # [('a',1), ('b',2)]
tuples_to_dict = dict([('a', 1), ('b', 2)])      # {'a':1, 'b':2}
```

### Performance Comparison
```python
import timeit

# Membership testing
list_time = timeit.timeit('999999 in my_list', 
                         'my_list = list(range(1000000))', number=1000)
set_time = timeit.timeit('999999 in my_set', 
                        'my_set = set(range(1000000))', number=1000)

print(f"List: {list_time:.4f}s, Set: {set_time:.4f}s")
# Set is much faster for membership testing!
```

---

## Pro Tips 💡

1. **Use tuples** for fixed data that shouldn't change
2. **Use sets** when you need unique items or fast membership testing
3. **Use dictionaries** for key-value lookups
4. **Use lists** for ordered data that needs modification
5. **Dictionary keys** must be immutable (use tuples, strings, numbers, frozenset)
6. **List comprehension** is often more efficient than manual loops:
   ```python
   squares = [x**2 for x in range(10)]  # Better than loop
   ```
7. **Set comprehension** for unique values:
   ```python
   unique_squares = {x**2 for x in range(10)}
   ```
8. **Dictionary comprehension** for key-value creation:
   ```python
   squared_dict = {x: x**2 for x in range(10)}
   ```

---

## Practice Exercise 📝

Try to predict the output and explain why:

```python
# Exercise 1
list1 = [1, 2, 3]
list2 = list1
list1.append(4)
print(list2)  # What's the output?

# Exercise 2
tuple1 = (1, 2, 3)
tuple2 = tuple1
# tuple1.append(4)  # What happens?

# Exercise 3
set1 = {1, 2, 3}
set2 = set1
set1.add(4)
print(set2)  # What's the output?

# Exercise 4
dict1 = {'a': 1, 'b': 2}
dict2 = dict1
dict1['c'] = 3
print(dict2)  # What's the output?
```

---

Happy coding! Remember: **"Choose the right tool for the right job"** - pick the data structure that best fits your use case! 🎯