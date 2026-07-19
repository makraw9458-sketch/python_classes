# Creation
# my_dict = {
#     'name': 'John', 
#     'age': 30, 
#     'city': 'NYC'
# }
# mixed_dict = {'name': 'Alice', 1: 'one', (1,2): 'tuple_key'}
# empty_dict = {}

# Using dict() constructor
# dict_from_pairs = dict([('a', 1), ('b', 2)])
# dict_from_kwargs = dict(name='Bob', age=25)



# OPERATIONS

# Accessing
person = {'name': 'varun', 'age': 30, 'city': 'mumbai', 'country' : 'India'}

# Get values
# print(person['name'])          # 'Alice' (error if missing)
# print(person.get('agea'))       # 30 (returns None if missing)
# print(person.get('country', 'UK'))  # Default value

# Adding/Updating
# person['email'] = 'alice@email.com'  # Add new
# person['age'] = 31                   # Update existing
# person.update({'city': 'Paris', 'phone': '123'})

# Removing
# del person['city']             # Remove key (error if missing)
# popped = person.pop('age')     # Remove and return
# popped_item = person.popitem() # Remove and return last item
# person.clear()                 # Empty dict

# Iteration
# for key in person:
#     print(person[key])

# for key, value in person.items():
#     print(f"{key}: {value}")

# print(person.keys())

# keys = frozenset(person.keys())

# for key in keys: # Iterate keys
#     print(key, person[key])

# print(person.values())
# for value in person.values():  # Iterate values
#     print(value)

# Other operations
# print(len(person))                    # Number of items
# print('name' in person)              # Check if key exists
# print(list(person.keys()))            # Get all keys