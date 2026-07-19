
## Comparison Table 📊

| Feature | List | Tuple | Set | Dictionary | Frozenset |
|---------|------|-------|-----|------------|-----------|
| **Ordered** | Yes | Yes | No | Yes (3.7+) | No |
| **Mutable** | Yes | No | Yes | Yes | No |
| **Duplicates** | Yes | Yes | No | Keys: No | No |
| **Indexed** | Yes | Yes | No | By key | No |
| **Heterogeneous** | Yes | Yes | Yes | Yes | Yes |
| **Hashable** | No | Yes | No | Keys: Yes | Yes |
| **Memory Efficient** | Low | High | Medium | Low | High |
| **Speed (lookup)** | O(n) | O(n) | O(1) | O(1) | O(1) |

---

## When to Use Which? 🤔

| Data Structure | Best Used For |
|----------------|---------------|
| **List** | Ordered collections that need modification, stacking, queuing |
| **Tuple** | Fixed data, dictionary keys, multiple return values |
| **Set** | Unique items, membership testing, set operations |
| **Dictionary** | Key-value associations, lookups by unique identifier |
| **Frozenset** | Immutable unique collection, hashable sets |

---
