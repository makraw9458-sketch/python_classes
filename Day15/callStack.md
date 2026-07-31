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