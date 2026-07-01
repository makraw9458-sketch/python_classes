# Basic while loop
count = 0 # iterator
while count < 5:
    if count == 3:
        count += 1
        continue
    
    print(count)
    count += 1



# Infinite loop (be careful!)
# while True:
#     print("This will run forever")

# While with user input
# password = ""
# correctPWD = "secret"

# while password != correctPWD:
#     password = input("Enter password: ")
# print("Access granted!")