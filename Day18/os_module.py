# import os

# if os.path.exists('file.txt'):
#     size = os.path.getsize('file.txt')
#     print(f"file size = {size}")

#     os.rename('file.txt', 'new.txt')

#     os.remove('new.txt')

#     if os.path.exists('new.txt'):
#         print('error!')
#     else:
#         print("file deleted")

# else:
#     print('File not found')


# Copy file
import shutil
shutil.copy('file.txt', 'destination.txt')