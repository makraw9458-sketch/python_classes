print("program start")

# with open('missing.txt', 'r') as f:
#     content = f.read()

try:
    print("inside try start")
    with open('missing.txt', 'r') as f:
        content = f.read()
    print("inside try end")
except FileNotFoundError:
    print('File not found!')
except PermissionError:
    print('No permission to read file!')
except Exception as e:
    print(f'Error: {e}')

print("program end")