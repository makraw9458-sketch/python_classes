# Greatest number

# arr = [10, 5, 20, 8, 15]
# greatest = arr[0]  # Assume first element is greatest

# for num in arr:
#     if num > greatest:
#         greatest = num

# print("Greatest number = ", greatest)


# conditionals

# age = int(input("enter your age: "))

# if age > 18:
#     print("you are an adult")
# elif age == 18:
#     print("you are exactly 18yo")
#     print("so you are an adult")
# else:
#     print("you are not an adult")



# TASK (user login system)

# users = [
#     {"username": "john_doe", "password": "pass123"},
#     {"username": "jane_smith", "password": "secure456"},
#     {"username": "bob_wilson", "password": "mypass789"}
# ]

# db
user_name = "atif"
password = "Y"

# CTA
u_name_ip = input("enter your user name: ")


if user_name == u_name_ip:
    u_pass_ip = input("enter your user password: ")

    if password == u_pass_ip:
        print('successful access')
    else:
       print("access denied: wrong password")
else:
    print("access denied: wrong username")

# 

# user_id = "xyz"
# password_correct = True
# if user_id == "xyz":
#    if password_correct:
#        print("successful login")
# else:
#    print("access denied")
