# Python File I/O - Simple Guide

## Opening Files

```python
# Basic open
file = open('filename.txt', 'r')  # 'r' = read, 'w' = write, 'a' = append
# Always close!
file.close()

# Best practice - auto-closes
with open('filename.txt', 'r') as file:
    # do stuff here
    pass  # auto-closes when done
```

## Reading Files

```python
# Read entire file
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)

# Read line by line
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())  # strip() removes newline

# Read all lines into list
with open('file.txt', 'r') as f:
    lines = f.readlines()  # list of strings

# Read one line
with open('file.txt', 'r') as f:
    first_line = f.readline()
```

## Writing Files

```python
# Write (overwrites existing)
with open('file.txt', 'w') as f:
    f.write('Hello World\n')
    f.write('Second line')

# Write multiple lines
lines = ['line1\n', 'line2\n', 'line3\n']
with open('file.txt', 'w') as f:
    f.writelines(lines)

# Append (adds to end)
with open('file.txt', 'a') as f:
    f.write('This adds to the end\n')
```

## File Modes

```python
'r'  # Read (default)
'w'  # Write (overwrites)
'a'  # Append
'x'  # Create (fails if exists)
'r+' # Read and write
```

## Check if File Exists

```python
import os

if os.path.exists('file.txt'):
    print('File exists')
else:
    print('File not found')
```

## Common Operations

```python
# Get file size
import os
size = os.path.getsize('file.txt')

# Delete file
import os
os.remove('file.txt')

# Rename file
import os
os.rename('old.txt', 'new.txt')

# Copy file
import shutil
shutil.copy('source.txt', 'destination.txt')
```

## Error Handling

```python
try:
    with open('missing.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('File not found!')
except PermissionError:
    print('No permission to read file!')
except Exception as e:
    print(f'Error: {e}')
```

## Quick Examples

```python
# Read a text file
with open('data.txt', 'r') as f:
    data = f.read()

# Write to a text file
with open('output.txt', 'w') as f:
    f.write('Hello World')

# Append to a file
with open('log.txt', 'a') as f:
    f.write('New log entry\n')

# Read and count lines
with open('file.txt', 'r') as f:
    line_count = sum(1 for line in f)
    print(f'Lines: {line_count}')
```

## File Paths

```python
# Relative path
with open('folder/file.txt', 'r') as f:
    pass

# Absolute path (Windows)
with open('C:/Users/name/file.txt', 'r') as f:
    pass

# Absolute path (Mac/Linux)
with open('/home/user/file.txt', 'r') as f:
    pass

# Using os.path for cross-platform
import os
path = os.path.join('folder', 'subfolder', 'file.txt')
with open(path, 'r') as f:
    pass
```

## Binary Files

```python
# Read binary (images, etc.)
with open('image.jpg', 'rb') as f:
    binary_data = f.read()

# Write binary
with open('copy.jpg', 'wb') as f:
    f.write(binary_data)
```

**Remember:** Always use `with open()` - it handles closing files automatically!