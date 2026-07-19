# Creation
my_tuple = (1, 2, 3, 4, 5)
mixed_tuple = (1, "hello", 3.14, True)
single_tuple = (1,)           # Comma is necessary!
empty_tuple = ()

# print(id(my_tuple))

my_tuple = (6,7,8,9,0)

# print(id(my_tuple))

# Using tuple() constructor
tuple_from_list = tuple([1, 2, 3])

# Without parentheses (tuple packing)
coordinates = 10, 20, 30      # Also a tuple

# print(coordinates)


# common ops.
# Accessing (same as lists)
t = ('a', 'b', 'c', 'd')
# print(t[0])          # 'a'
# print(t[-1])         # 'd'
# print(t[1:3])        # ('b', 'c')

# Methods (limited due to immutability)
t.count('a')         # Count occurrences
t.index('b')         # Returns index

# Unpacking
a, b, c = 1, 2, 3  # a=1, b=2, c=3
# print(type(a))





# eg
