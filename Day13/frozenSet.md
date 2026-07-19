
## 5. **FROZENSET** ❄️

### Definition
Immutable version of set.

### Properties
- **Unordered**: Same as set
- **Immutable**: Cannot be modified after creation
- **Hashable**: Can be used as dictionary keys
- **No Duplicates**: Automatically removes duplicates

### Syntax
```python
# Creation
my_frozenset = frozenset([1, 2, 3, 4, 5])
empty_frozenset = frozenset()
```

### Use Cases
- Dictionary keys (when you need a set as key)
- Set of sets
- Storing constant collections
- When immutability is required
