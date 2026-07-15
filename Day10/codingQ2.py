password = "secret123"
attempts = 3

while attempts > 0:
    attempts -= 1

    user_answer = input("enter your password: ")
    if user_answer == "":
        continue
    
    if user_answer == password:
        print("Access Granted!")
        break
    else :
        print (f"Incorrect. Attempts remaining: {attempts}")

    if(attempts == 0):
        print("Access Blocked.")