
## 4. Recursion Deep Dive {#recursion}

### Recursion Under the Hood

Recursion uses the call stack to store intermediate states.

```python
import sys
import time

def factorial_recursive(n):
    """
    Classic recursive factorial with detailed tracking
    
    How it works:
    factorial(5) = 5 * factorial(4)
    factorial(4) = 4 * factorial(3)
    factorial(3) = 3 * factorial(2)
    factorial(2) = 2 * factorial(1)
    factorial(1) = 1
    
    Backtracking:
    factorial(1) returns 1
    factorial(2) returns 2 * 1 = 2
    factorial(3) returns 3 * 2 = 6
    factorial(4) returns 4 * 6 = 24
    factorial(5) returns 5 * 24 = 120
    """
    print(f"Entering factorial({n})")
    
    # Base case
    if n <= 1:
        print(f"Base case reached: factorial({n}) returns 1")
        return 1
    
    # Recursive case
    result = n * factorial_recursive(n - 1)
    print(f"Factorial({n}) = {n} * factorial({n-1}) = {result}")
    return result

# Run with tracking
print("Recursive Factorial Calculation:")
print(f"Result: {factorial_recursive(5)}")
```

### Visualizing Recursion with Stack Frames

```python
def visualize_recursion(func, *args, depth=0):
    """Visualize recursive calls with indentation"""
    prefix = "  " * depth
    print(f"{prefix}Calling {func.__name__}{args}")
    
    if depth > 5:
        print(f"{prefix}Too deep, returning")
        return
    
    # Handle the recursion
    if hasattr(func, '__call__'):
        result = func(*args)
        print(f"{prefix}Returned {result}")
        return result

# Fibonacci with visualization
def fibonacci(n, depth=0):
    """Fibonacci sequence with visualization"""
    indent = "  " * depth
    print(f"{indent}fibonacci({n}) called")
    
    if n <= 1:
        print(f"{indent}Base case: fibonacci({n}) = {n}")
        return n
    
    print(f"{indent}Computing fibonacci({n}) = fibonacci({n-1}) + fibonacci({n-2})")
    
    # Left branch
    print(f"{indent}Going left...")
    left = fibonacci(n-1, depth+1)
    
    # Right branch
    print(f"{indent}Going right...")
    right = fibonacci(n-2, depth+1)
    
    result = left + right
    print(f"{indent}fibonacci({n}) = {left} + {right} = {result}")
    return result

print("\n=== Fibonacci Recursion ===")
print(f"Fibonacci(5) = {fibonacci(5)}")
```
