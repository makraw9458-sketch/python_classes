# The Complete Under-the-Hood Guide to Functions in Python

## Table of Contents
1. [Function Fundamentals](#fundamentals)
2. [Function Anatomy](#anatomy)
3. [The Call Stack](#call-stack)
4. [Recursion Deep Dive](#recursion)
5. [Built-in Functions Examples](#built-in)
6. [User-Defined Functions Examples](#user-defined)
7. [Advanced Concepts](#advanced)

---

## 1. Function Fundamentals {#fundamentals}

### What Happens When You Define a Function?

When Python encounters a function definition, it:
1. Creates a **function object** in memory
2. Stores the **code object** (bytecode)
3. Sets up the **function's namespace**
4. Binds the function name to the function object

```python
def my_function(x, y):
    """This is a docstring"""
    result = x + y
    return result

# Under the hood:
# 1. Python creates a function object
# 2. The function object has:
#    - __code__: code object with bytecode
#    - __name__: "my_function"
#    - __doc__: "This is a docstring"
#    - __defaults__: default argument values
#    - __closure__: closure cells (if any)
```

---

## 2. Function Anatomy {#anatomy}

### Complete Function Structure

```python
def function_name(param1, param2=default_value, *args, **kwargs):
    """
    Docstring: Describes what the function does
    """
    # Local variables
    local_var = "I'm local"
    
    # Function body
    result = param1 + param2
    
    # Return statement
    return result
```

### Function Object Internals

```python
def examine_function(func):
    """Examine the internal structure of a function"""
    print(f"Function name: {func.__name__}")
    print(f"Docstring: {func.__doc__}")
    print(f"Default arguments: {func.__defaults__}")
    print(f"Code object: {func.__code__}")
    print(f"Global namespace: {func.__globals__ is globals()}")
    print(f"Local variables: {func.__code__.co_varnames}")
    print(f"Number of arguments: {func.__code__.co_argcount}")
    print(f"Bytecode: {func.__code__.co_code}")

def sample_func(a, b=10):
    """Sample function for inspection"""
    c = a + b
    return c

examine_function(sample_func)
```

### The Code Object

```python
import dis

def add_numbers(x, y):
    z = x + y
    return z

# Disassemble to see bytecode
print("Bytecode instructions:")
dis.dis(add_numbers)

# Output shows:
# LOAD_FAST (x)    -> loads local variable x
# LOAD_FAST (y)    -> loads local variable y
# BINARY_OP (+)    -> performs addition
# STORE_FAST (z)   -> stores result in z
# LOAD_FAST (z)    -> loads z for return
# RETURN_VALUE     -> returns the value
```

---

## 3. The Call Stack {#call-stack}

### Understanding the Call Stack

The call stack is a LIFO (Last-In-First-Out) data structure that tracks function calls.

```python
import inspect
import sys

def function_a():
    print("Entering A")
    print(f"A's local variables: {locals()}")
    function_b()
    print("Exiting A")

def function_b():
    print("Entering B")
    print(f"B's local variables: {locals()}")
    function_c()
    print("Exiting B")

def function_c():
    print("Entering C")
    print(f"C's local variables: {locals()}")
    
    # Inspect the call stack
    print("\n--- Call Stack ---")
    stack = inspect.stack()
    for frame in stack:
        print(f"Function: {frame.function}, File: {frame.filename}, Line: {frame.lineno}")
    
    print("Exiting C")

# Call the functions
function_a()
```

### Manual Stack Visualization

```python
class Stack:
    """Custom stack implementation to visualize call stack"""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        print(f"PUSH: {item}")
        self.display()
    
    def pop(self):
        if self.items:
            item = self.items.pop()
            print(f"POP: {item}")
            self.display()
            return item
    
    def display(self):
        print(f"Stack: {self.items}")

# Simulate function calls with stack
stack = Stack()

def function_x():
    stack.push("Function X Frame")
    # Simulate work
    function_y()
    stack.pop()

def function_y():
    stack.push("Function Y Frame")
    function_z()
    stack.pop()

def function_z():
    stack.push("Function Z Frame")
    # Simulate work
    stack.pop()

# Run simulation
function_x()
```

### Frame Objects in Depth

```python
import sys
import traceback

def frame_inspection():
    """Inspect frame objects in the call stack"""
    current_frame = sys._getframe()
    
    print("=== Frame Inspection ===")
    print(f"Frame object: {current_frame}")
    print(f"Function name: {current_frame.f_code.co_name}")
    print(f"Filename: {current_frame.f_code.co_filename}")
    print(f"Line number: {current_frame.f_lineno}")
    print(f"Local variables: {current_frame.f_locals}")
    print(f"Global variables: {current_frame.f_globals}")
    
    # Traverse the call stack
    print("\n=== Call Stack Trace ===")
    frame = current_frame
    level = 0
    while frame:
        indent = "  " * level
        print(f"{indent}Level {level}: {frame.f_code.co_name}()")
        frame = frame.f_back
        level += 1

def outer_function():
    def inner_function():
        def deeper_function():
            frame_inspection()
        deeper_function()
    inner_function()

outer_function()
```

---

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

### Tail Recursion and Optimizations

```python
def factorial_tail_recursive(n, accumulator=1):
    """
    Tail-recursive factorial (not optimized in Python by default)
    
    The recursive call is the last operation, allowing potential optimization
    """
    if n == 0:
        return accumulator
    return factorial_tail_recursive(n - 1, n * accumulator)

def optimized_recursion(original_func):
    """Decorator to optimize tail-recursive functions using trampolining"""
    class Trampoline:
        def __init__(self, func):
            self.func = func
        
        def __call__(self, *args, **kwargs):
            result = self.func(*args, **kwargs)
            while callable(result):
                result = result()
            return result
    
    return Trampoline(original_func)

@optimized_recursion
def tail_factorial(n, acc=1):
    if n == 0:
        return acc
    return lambda: tail_factorial(n-1, n*acc)

print(f"Tail-recursive factorial(10): {tail_factorial(10)}")
```

### Recursion vs Iteration - Performance Analysis

```python
import time
import functools

def timeit(func):
    """Decorator to time function execution"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timeit
def factorial_recursive(n):
    """Recursive factorial"""
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

@timeit
def factorial_iterative(n):
    """Iterative factorial"""
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# Compare performance
print("=== Performance Comparison ===")
print(f"Recursive factorial(10): {factorial_recursive(10)}")
print(f"Iterative factorial(10): {factorial_iterative(10)}")

# Check recursion limit
print(f"\nRecursion limit: {sys.getrecursionlimit()}")

def measure_recursion_depth():
    """Measure how deep recursion can go"""
    def deep_recursion(n):
        if n == 0:
            return 0
        return deep_recursion(n-1) + 1
    
    try:
        depth = deep_recursion(1000)
        print(f"Recursion depth achieved: {depth}")
    except RecursionError:
        print("Recursion limit reached!")

measure_recursion_depth()
```

---

## 5. Built-in Functions Examples {#built-in}

### Comprehensive Built-in Functions Deep Dive

```python
import builtins
import math
import random
from functools import reduce

class BuiltinFunctionsDemo:
    """Demonstrate all major built-in functions"""
    
    @staticmethod
    def map_filter_reduce_demo():
        """Map, Filter, and Reduce - The functional trinity"""
        numbers = range(1, 11)
        
        # Map: Apply function to each element
        squared = list(map(lambda x: x**2, numbers))
        print(f"Map (squares): {squared}")
        
        # Filter: Filter elements based on condition
        even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 21)))
        print(f"Filter (even numbers): {even_numbers}")
        
        # Reduce: Reduce to single value
        sum_of_numbers = reduce(lambda x, y: x + y, range(1, 11))
        print(f"Reduce (sum): {sum_of_numbers}")
    
    @staticmethod
    def any_all_demo():
        """Any and All - Logical operations on iterables"""
        # Any: True if any element is True
        bool_list1 = [False, False, True, False]
        bool_list2 = [False, False, False, False]
        
        print(f"Any({bool_list1}): {any(bool_list1)}")
        print(f"Any({bool_list2}): {any(bool_list2)}")
        
        # All: True if all elements are True
        bool_list3 = [True, True, True]
        bool_list4 = [True, False, True]
        
        print(f"All({bool_list3}): {all(bool_list3)}")
        print(f"All({bool_list4}): {all(bool_list4)}")
    
    @staticmethod
    def zip_enumerate_demo():
        """Zip and Enumerate - Combining and tracking iterables"""
        names = ['Alice', 'Bob', 'Charlie']
        scores = [95, 87, 92]
        
        # Zip: Combine iterables
        zipped = list(zip(names, scores))
        print(f"Zipped: {zipped}")
        
        # Enumerate: Add index to iterable
        for idx, (name, score) in enumerate(zip(names, scores), start=1):
            print(f"#{idx}: {name} scored {score}")
    
    @staticmethod
    def sorted_reversed_demo():
        """Sorted and Reversed - Ordering operations"""
        # Sorted: Returns sorted list
        numbers = [3, 1, 4, 1, 5, 9, 2, 6]
        
        ascending = sorted(numbers)
        descending = sorted(numbers, reverse=True)
        absolute_sorted = sorted(numbers, key=abs)  # Sort by absolute value
        
        print(f"Original: {numbers}")
        print(f"Sorted ascending: {ascending}")
        print(f"Sorted descending: {descending}")
        print(f"Sorted by absolute: {absolute_sorted}")
        
        # Reversed: Returns reverse iterator
        text = "Hello, World!"
        print(f"Reversed text: {''.join(reversed(text))}")
    
    @staticmethod
    def isinstance_issubclass_demo():
        """Type checking with isinstance and issubclass"""
        class Animal: pass
        class Dog(Animal): pass
        class Cat(Animal): pass
        
        dog = Dog()
        
        print(f"dog is Dog: {isinstance(dog, Dog)}")
        print(f"dog is Animal: {isinstance(dog, Animal)}")
        print(f"Dog is subclass of Animal: {issubclass(Dog, Animal)}")
        print(f"Cat is subclass of Dog: {issubclass(Cat, Dog)}")
    
    @staticmethod
    def eval_exec_compile_demo():
        """Dynamic code execution"""
        # Eval: Evaluate expression
        expression = "3 * 4 + 5"
        result = eval(expression)
        print(f"Eval '{expression}': {result}")
        
        # Exec: Execute code block
        code_block = """
        x = 10
        y = 20
        z = x + y
        """
        namespace = {}
        exec(code_block, namespace)
        print(f"Exec namespace: {namespace}")
        
        # Compile: Compile code for later execution
        compiled = compile("print('Hello from compiled code')", '<string>', 'exec')
        exec(compiled)
    
    @staticmethod
    def property_setattr_getattr_demo():
        """Dynamic attribute manipulation"""
        class Person:
            def __init__(self, name):
                self.name = name
            
            @property
            def greeting(self):
                return f"Hello, I'm {self.name}"
        
        person = Person("Alice")
        
        # Getattr: Get attribute dynamically
        name = getattr(person, 'name')
        greeting = getattr(person, 'greeting')
        
        print(f"Name: {name}")
        print(f"Greeting: {greeting}")
        
        # Setattr: Set attribute dynamically
        setattr(person, 'age', 30)
        print(f"Age set: {person.age}")
        
        # Hasattr: Check attribute existence
        print(f"Has age? {hasattr(person, 'age')}")
        print(f"Has address? {hasattr(person, 'address')}")
    
    @staticmethod
    def all_builtins():
        """List all built-in functions"""
        print("=== All Built-in Functions ===")
        builtin_functions = []
        for item in dir(builtins):
            if callable(getattr(builtins, item)):
                builtin_functions.append(item)
        
        # Print in organized format
        for i, func in enumerate(sorted(builtin_functions), 1):
            print(f"{i:3}. {func}")
        
        return len(builtin_functions)

# Run demonstrations
demo = BuiltinFunctionsDemo()
demo.map_filter_reduce_demo()
demo.any_all_demo()
demo.zip_enumerate_demo()
demo.sorted_reversed_demo()
demo.isinstance_issubclass_demo()
demo.eval_exec_compile_demo()
demo.property_setattr_getattr_demo()
print(f"\nTotal built-in functions: {demo.all_builtins()}")
```

---

## 6. User-Defined Functions Examples {#user-defined}

### Advanced User-Defined Functions

```python
from functools import wraps, lru_cache
from typing import Callable, Any, Dict, List
import time
import inspect

class AdvancedFunctionExamples:
    """Comprehensive user-defined function examples"""
    
    @staticmethod
    def decorator_factory():
        """Create and use custom decorators"""
        
        # Basic decorator
        def timer(func):
            """Time function execution"""
            @wraps(func)
            def wrapper(*args, **kwargs):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter()
                print(f"{func.__name__} took {end - start:.6f} seconds")
                return result
            return wrapper
        
        # Parameterized decorator
        def repeat(times: int):
            """Repeat function execution N times"""
            def decorator(func):
                @wraps(func)
                def wrapper(*args, **kwargs):
                    results = []
                    for i in range(times):
                        print(f"Running iteration {i+1}/{times}")
                        results.append(func(*args, **kwargs))
                    return results
                return wrapper
            return decorator
        
        # Class decorator
        def singleton(cls):
            """Ensure only one instance exists"""
            instances = {}
            @wraps(cls)
            def wrapper(*args, **kwargs):
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
                return instances[cls]
            return wrapper
        
        @timer
        def long_running_task():
            time.sleep(0.1)
            return "Done"
        
        @repeat(3)
        def multiply_by_2(x):
            return x * 2
        
        @singleton
        class Database:
            def __init__(self, name):
                self.name = name
        
        # Test the decorators
        print("Timer decorator:")
        long_running_task()
        
        print("\nRepeat decorator:")
        results = multiply_by_2(5)
        print(f"Results: {results}")
        
        print("\nSingleton decorator:")
        db1 = Database("Primary")
        db2 = Database("Secondary")
        print(f"db1 is db2: {db1 is db2}")
        print(f"db1 name: {db1.name}")
        print(f"db2 name: {db2.name}")
    
    @staticmethod
    def closure_examples():
        """Demonstrate closures and lexical scoping"""
        
        def counter():
            """Create a counter with closure"""
            count = 0
            
            def increment():
                nonlocal count
                count += 1
                return count
            
            def decrement():
                nonlocal count
                count -= 1
                return count
            
            def reset():
                nonlocal count
                count = 0
                return count
            
            def get_count():
                return count
            
            return {
                'increment': increment,
                'decrement': decrement,
                'reset': reset,
                'get_count': get_count
            }
        
        # Create counters
        counter1 = counter()
        counter2 = counter()
        
        print("Counter 1 operations:")
        for _ in range(3):
            print(f"Count: {counter1['increment']()}")
        
        print(f"Counter 2 count: {counter2['get_count']()}")
        counter2['decrement']()
        print(f"Counter 2 after decrement: {counter2['get_count']()}")
    
    @staticmethod
    def generator_functions():
        """Advanced generator examples"""
        
        def fibonacci_generator(limit: int):
            """Generate Fibonacci numbers up to limit"""
            a, b = 0, 1
            count = 0
            while count < limit:
                yield a
                a, b = b, a + b
                count += 1
        
        def custom_range(start: int, stop: int, step: int = 1):
            """Custom range generator with more features"""
            current = start
            while current < stop:
                yield current
                current += step
        
        def coroutine_example():
            """Coroutine for accumulating numbers"""
            total = 0
            while True:
                value = yield total
                if value is None:
                    break
                total += value
        
        # Test generators
        print("Fibonacci generator:")
        fib = fibonacci_generator(10)
        print(list(fib))
        
        print("\nCustom range:")
        for num in custom_range(2, 20, 3):
            print(num, end=' ')
        print()
        
        print("\nCoroutine example:")
        coro = coroutine_example()
        next(coro)  # Prime the coroutine
        
        numbers = [1, 2, 3, 4, 5]
        for num in numbers:
            print(f"Sending {num}, total: {coro.send(num)}")
        coro.close()
    
    @staticmethod
    def lambda_functions():
        """Advanced lambda function usage"""
        
        # Lambda with multiple operations
        complex_lambda = lambda x: (x**2 + 2*x + 1) / (x + 1)
        
        # Lambda in data structures
        operations = {
            'add': lambda x, y: x + y,
            'subtract': lambda x, y: x - y,
            'multiply': lambda x, y: x * y,
            'divide': lambda x, y: x / y if y != 0 else float('inf')
        }
        
        # Lambda with sorting key
        people = [
            {'name': 'Alice', 'age': 30},
            {'name': 'Bob', 'age': 25},
            {'name': 'Charlie', 'age': 35}
        ]
        sorted_by_age = sorted(people, key=lambda p: p['age'])
        
        # Lambda for filtering
        numbers = range(1, 21)
        perfect_squares = filter(lambda x: math.isqrt(x)**2 == x, numbers)
        
        # Test lambda functions
        print(f"Complex lambda(3): {complex_lambda(3)}")
        
        print("\nOperation dictionary:")
        print(f"Add: {operations['add'](5, 3)}")
        print(f"Divide by zero: {operations['divide'](5, 0)}")
        
        print(f"\nSorted people by age: {sorted_by_age}")
        print(f"Perfect squares: {list(perfect_squares)}")
    
    @staticmethod
    def function_annotations():
        """Type hints and annotations"""
        
        def process_data(data: List[int], 
                       multiplier: float = 1.0) -> List[float]:
            """Process integer list with type annotations"""
            return [x * multiplier for x in data]
        
        def complex_operation(*args: int, 
                             **kwargs: float) -> Dict[str, Any]:
            """Complex operation with annotations"""
            total = sum(args)
            average = total / len(args) if args else 0
            product = 1
            
            for num in args:
                product *= num
            
            return {
                'sum': total,
                'average': average,
                'product': product,
                'kwargs': kwargs,
                'argument_count': len(args)
            }
        
        # Access annotations
        print(f"process_data annotations: {process_data.__annotations__}")
        print(f"complex_operation annotations: {complex_operation.__annotations__}")
        
        # Use functions
        result = process_data([1, 2, 3, 4, 5], 2.5)
        print(f"Processed data: {result}")
        
        complex_result = complex_operation(1, 2, 3, 4, 5, multiplier=2.0)
        print(f"Complex operation result: {complex_result}")
    
    @staticmethod
    def recursive_examples():
        """Advanced recursive function examples"""
        
        @lru_cache(maxsize=None)
        def memoized_fibonacci(n: int) -> int:
            """Memoized Fibonacci - exponential to linear"""
            if n <= 1:
                return n
            return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
        
        def graph_dfs(graph: Dict, node: str, visited: set = None):
            """Graph DFS using recursion"""
            if visited is None:
                visited = set()
            
            print(f"Visiting: {node}")
            visited.add(node)
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    graph_dfs(graph, neighbor, visited)
            
            return visited
        
        def nested_sum(nested_list: List) -> int:
            """Sum all numbers in nested list"""
            total = 0
            for item in nested_list:
                if isinstance(item, list):
                    total += nested_sum(item)
                else:
                    total += item
            return total
        
        # Test recursion examples
        print(f"Memoized Fibonacci(50): {memoized_fibonacci(50)}")
        
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }
        print("\nGraph DFS traversal:")
        graph_dfs(graph, 'A')
        
        nested_list = [1, [2, 3], [4, [5, 6, [7, 8]]]]
        print(f"\nNested list sum: {nested_sum(nested_list)}")

# Run all examples
examples = AdvancedFunctionExamples()
examples.decorator_factory()
print("\n" + "="*50 + "\n")
examples.closure_examples()
print("\n" + "="*50 + "\n")
examples.generator_functions()
print("\n" + "="*50 + "\n")
examples.lambda_functions()
print("\n" + "="*50 + "\n")
examples.function_annotations()
print("\n" + "="*50 + "\n")
examples.recursive_examples()
```

---

## 7. Advanced Concepts {#advanced}

### Metaprogramming with Functions

```python
class MetaFunctionExamples:
    """Advanced metaprogramming with functions"""
    
    @staticmethod
    def function_factory():
        """Create functions dynamically"""
        
        def create_arithmetic_operation(op: str):
            """Create arithmetic operation function"""
            if op == 'add':
                return lambda x, y: x + y
            elif op == 'subtract':
                return lambda x, y: x - y
            elif op == 'multiply':
                return lambda x, y: x * y
            elif op == 'divide':
                return lambda x, y: x / y if y != 0 else float('inf')
            else:
                raise ValueError(f"Unknown operation: {op}")
        
        # Create functions dynamically
        add_func = create_arithmetic_operation('add')
        multiply_func = create_arithmetic_operation('multiply')
        
        print(f"Dynamic add: {add_func(10, 5)}")
        print(f"Dynamic multiply: {multiply_func(10, 5)}")
        
        # Function composition
        def compose(f: Callable, g: Callable) -> Callable:
            """Compose two functions: f(g(x))"""
            return lambda x: f(g(x))
        
        def square(x): return x ** 2
        def double(x): return x * 2
        
        square_then_double = compose(double, square)
        double_then_square = compose(square, double)
        
        print(f"square(3)=9, double(9)=18: {square_then_double(3)}")
        print(f"double(3)=6, square(6)=36: {double_then_square(3)}")
    
    @staticmethod
    def partial_application():
        """Implement partial application (currying)"""
        
        def curry(func: Callable):
            """Curry a function"""
            def curried(*args):
                if len(args) >= func.__code__.co_argcount:
                    return func(*args)
                return lambda *more: curried(*(args + more))
            return curried
        
        @curry
        def add_three_numbers(a, b, c):
            return a + b + c
        
        # Partial application
        add_5 = add_three_numbers(5)
        add_5_and_3 = add_5(3)
        result = add_5_and_3(7)
        
        print(f"Curried addition: add_three_numbers(5)(3)(7) = {result}")
        
        # Another example with built-in
        def power(base: float, exponent: float) -> float:
            return base ** exponent
        
        squared = lambda x: power(x, 2)
        cubed = lambda x: power(x, 3)
        
        print(f"Square of 5: {squared(5)}")
        print(f"Cube of 5: {cubed(5)}")
    
    @staticmethod
    def function_introspection():
        """Deep function introspection"""
        
        def complex_function(a: int, b: str = "default", *args, **kwargs) -> bool:
            """
            This is a complex function for demonstration.
            
            Args:
                a: An integer parameter
                b: A string parameter with default
                *args: Variable positional arguments
                **kwargs: Variable keyword arguments
            
            Returns:
                bool: Always returns True for this example
            """
            return True
        
        # Introspection
        print("=== Function Introspection ===")
        print(f"Name: {complex_function.__name__}")
        print(f"Docstring: {complex_function.__doc__}")
        print(f"Annotations: {complex_function.__annotations__}")
        print(f"Default arguments: {complex_function.__defaults__}")
        print(f"Closure: {complex_function.__closure__}")
        print(f"Globals: {complex_function.__globals__ is globals()}")
        print(f"Module: {complex_function.__module__}")
        print(f"Qualified name: {complex_function.__qualname__}")
        
        # Signature introspection
        signature = inspect.signature(complex_function)
        print(f"\nSignature: {signature}")
        
        for param_name, param in signature.parameters.items():
            print(f"  {param_name}: {param.kind} = {param.default if param.default != inspect.Parameter.empty else 'No default'}")
        
        # Code object introspection
        code = complex_function.__code__
        print(f"\nCode object details:")
        print(f"  Argument count: {code.co_argcount}")
        print(f"  Var args: {code.co_varnames}")
        print(f"  Local variables: {code.co_localsplusnames}")
        print(f"  Filename: {code.co_filename}")
        print(f"  First line: {code.co_firstlineno}")
    
    @staticmethod
    def context_managers():
        """Functions as context managers"""
        
        class FunctionTimer:
            """Context manager for timing functions"""
            def __enter__(self):
                self.start = time.perf_counter()
                return self
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                self.end = time.perf_counter()
                self.duration = self.end - self.start
                print(f"Duration: {self.duration:.6f} seconds")
        
        def with_context_manager():
            """Use context manager with functions"""
            with FunctionTimer() as timer:
                time.sleep(0.1)
                print("Inside context manager")
            print(f"Time taken: {timer.duration:.6f} seconds")
        
        # Context manager using generator (contextlib)
        from contextlib import contextmanager
        
        @contextmanager
        def timed_operation(name: str):
            """Context manager as generator"""
            print(f"Starting: {name}")
            start = time.perf_counter()
            try:
                yield
            finally:
                end = time.perf_counter()
                print(f"Finished: {name} took {end - start:.6f} seconds")
        
        with timed_operation("Sleep operation"):
            time.sleep(0.05)
            print("Operation running")
        
        with_context_manager()

# Run meta examples
meta = MetaFunctionExamples()
meta.function_factory()
print("\n" + "="*50 + "\n")
meta.partial_application()
print("\n" + "="*50 + "\n")
meta.function_introspection()
print("\n" + "="*50 + "\n")
meta.context_managers()
```

### Complete Function Performance Analysis

```python
import timeit
import functools
from typing import Callable, Any

class FunctionPerformance:
    """Analyze function performance"""
    
    @staticmethod
    def performance_analysis():
        """Comprehensive performance analysis"""
        
        # Different implementations of factorial
        def factorial_iterative(n: int) -> int:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result
        
        def factorial_recursive(n: int) -> int:
            if n <= 1:
                return 1
            return n * factorial_recursive(n - 1)
        
        @functools.lru_cache(maxsize=None)
        def factorial_memoized(n: int) -> int:
            if n <= 1:
                return 1
            return n * factorial_memoized(n - 1)
        
        def factorial_reduce(n: int) -> int:
            from functools import reduce
            return reduce(lambda x, y: x * y, range(2, n + 1), 1)
        
        # Performance testing
        n = 500
        
        functions = {
            'Iterative': factorial_iterative,
            'Recursive': factorial_recursive,
            'Memoized': factorial_memoized,
            'Reduce': factorial_reduce
        }
        
        print("=== Performance Analysis ===")
        print(f"Calculating factorial({n})")
        
        for name, func in functions.items():
            if name == 'Recursive' and n > 1000:
                print(f"{name}: Skipped (too deep)")
                continue
            
            time_taken = timeit.timeit(
                lambda: func(n), 
                number=1000
            )
            result = func(n) if n <= 20 else "Too large"
            print(f"{name:12} | Time: {time_taken:.6f}s | Result: {result}")
    
    @staticmethod
    def memory_analysis():
        """Analyze memory usage of functions"""
        import tracemalloc
        
        def recursive_memory_test(n: int):
            """Recursive function for memory testing"""
            if n <= 0:
                return []
            return recursive_memory_test(n - 1) + [n]
        
        def iterative_memory_test(n: int):
            """Iterative function for memory testing"""
            result = []
            for i in range(1, n + 1):
                result.append(i)
            return result
        
        n = 500
        
        print("\n=== Memory Analysis ===")
        
        # Test recursive
        tracemalloc.start()
        recursive_memory_test(n)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Recursive | Peak: {peak / 1024:.2f} KB | Current: {current / 1024:.2f} KB")
        
        # Test iterative
        tracemalloc.start()
        iterative_memory_test(n)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Iterative | Peak: {peak / 1024:.2f} KB | Current: {current / 1024:.2f} KB")

# Run performance analysis
perf = FunctionPerformance()
perf.performance_analysis()
perf.memory_analysis()
```

---

## Summary

This comprehensive guide covers:

1. **Function Fundamentals**: How Python creates and manages function objects
2. **Function Anatomy**: Complete breakdown of function structure and internals
3. **Call Stack**: Detailed visualization and understanding of the stack
4. **Recursion**: Deep dive with visualizations and optimization techniques
5. **Built-in Functions**: Complete coverage with practical examples
6. **User-Defined Functions**: Advanced patterns with decorators, closures, generators
7. **Advanced Concepts**: Metaprogramming, partial application, introspection

### Key Takeaways

- Functions are first-class objects in Python
- The call stack is crucial for understanding program flow
- Recursion uses the stack and requires careful handling
- Built-in functions are optimized and should be preferred when possible
- Advanced patterns enable powerful and elegant code

### Performance Considerations

- Recursion: Elegant but stack-limited
- Iteration: Generally faster for large operations
- Memoization: Trade memory for speed
- Built-in functions: C-optimized and fastest

### Best Practices

1. Use appropriate recursion depth
2. Leverage built-in functions when possible
3. Use function annotations for clarity
4. Implement generators for memory efficiency
5. Use decorators for cross-cutting concerns

This guide provides a solid foundation for understanding and mastering functions in Python, from the basics to advanced metaprogramming techniques.