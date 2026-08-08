# n! = 1 * 2 * 3 ... * n-1 * n  = n * (n-1)!
# .
# .
# .
# 6! = 6 * 5 * 4 * 3 * 2 * 1    = 6 * 5!
# 5! = 5 * 4 * 3 * 2 * 1        = 5 * 4!
# 4! = 4 * 3 * 2 * 1            = 4 * 3!
# 3! = 3 * 2 * 1                = 3 * 2!
# 2! = 2 * 1                    = 2 * 1!
# 1! = 1                        = 1 * 0!
# 0! = 1                        = 1

def factorial_recursive(n):
    # Base case
    if (n == 0 or n == 1):
        return 1
    
    # Recursive case
    result = n * factorial_recursive(n - 1)
    return result

# Run with tracking
print("Recursive Factorial Calculation:")
print(f"Result: {factorial_recursive(5)}")



# step 1
# n =5, 
#  5 * fact(4)

# step 2
# n = 4
# 4 * fact(3)






# def factorial_recursive_explain(n):
    
#     print(f"Entering factorial({n})")
    
#     # Base case
#     if n <= 1:
#         print(f"Base case reached: factorial({n}) returns 1")
#         return 1
    
#     # Recursive case
#     result = n * factorial_recursive(n - 1)
#     print(f"Factorial({n}) = {n} * factorial({n-1}) = {result}")
#     return result