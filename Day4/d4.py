# a = b = c = 10

# print(a,b,c)

# a = 5
# print(a,b,c)

# a, b,  c = 10, 20, 30

# print(a,b,c)

# del a
# print(a,b,c)



# age = int(input("enter your age: "))

# if age > 18:
#     print("you are an adult")
# elif age == 18:
#     print("you are exactly 18yo")
#     print("so you are an adult")
# else:
#     print("you are not an adult")


# match cases

# number = 2

# if number == 1:
#     print("One")
# elif number == 2 or 3:
#     print("Two or Three")
# else:
#     print("Other number")
    



# match number:
#     case 1:
#         print("One")
#     case 2 | 3:
#         print("Two or Three")
#     case _:
#         print("Other number")







a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))

print(a,b)

# code for swap
# python way
# a, b = b, a

# using 3rd variable
# c = a
# a = b
# b = c

# without using 3rd variable
# a = 10
# b = 20

a = a + b
# a = 30
# b = 20

b = a - b
# a = 30
# b = 10

a = a - b
# swap done

print(a,b)