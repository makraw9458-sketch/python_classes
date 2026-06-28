# identity op

# is - returns True if both variables refer to the same object
# is not - returns True if both variables refer to different objects

a = [1, 2, 3] #10
c = [1, 2, 3] # c is a new object with same values
b = a = c     # b references the same object as a

print(a is b)      # True (same object)             true
print(a is c)      # False (different objects)      true
print(a is not c)  # True (different objects)       false
print(a == c)      # True (same values)             true

# is vs ==
# == compares values/content
# is compares identity/memory location

# Example with lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)  # True (same values)
print(list1 is list2)  # False (different objects in memory)
print(list1 is list3)  # True (same object)

# Example with strings (interned strings)
# str1 = "hello"
# str2 = "hello"
# str3 = "".join(["h", "e", "l", "l", "o"])

# print(str1 == str2)  # True
# print(str1 is str2)  # True (Python interns small strings)
# print(str1 is str3)  # False (created differently)
# print(str1 == str3)  # True


# CHECKING FOR SINGLETON OBJ
# True, False, and None are singletons
x = True
y = True

print(x is y)  # True (both point to same True object)

# Checking boolean values
flag = True
if (flag is True):  # Valid but usually unnecessary
    print("Flag is True")

# Usually just write:
if (flag):  # More Pythonic
    print("Flag is True")


# UNDERSTANDING OBJ IDENTITY
# Every object has a unique ID
a = [1, 2, 3]
b = [1, 2, 3]
# a = 99999999999999
# b = 99999999999999
# c = 10

print(id(a))  
print(id(b))  

print(id(a[0]))
print(id(b[0]))
print(id(1))
# print(id(c))  # Different from a

print(id(a) == id(b))  # True
print(a is b)          # True (equivalent to id check)

# Python caches small integers (-5 to 256)
x = 256
y = 256
print(x is y)  # True (cached)

x = 257
y = 257
print(x is y)  # False (not cached, may vary by implementation)

print("=================================")
# Strings are interned in some cases
s1 = "hello"
s2 = "hello"

print(s1 is s2)  # True (interned)
print("=================================")


s1 = "hello world"
s2 = "hello world"
print(s1 is s2)  # May be True or False (implementation dependent)

# Always use '==' for string comparison!