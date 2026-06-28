# TERNARY OPERATOR
# whats unary and binary op?
# a = not True
# a= 1+2




# Syntax
# value_if_true if condition else value_if_false

# Example
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Adult

# Traditional if-else equivalent
if age >= 18:
    status = "Adult"
else:
    status = "Minor"


# common use cases
# Simple assignment
score = 85
grade = "Pass" if score >= 50 else "Fail"
print(grade)  # Pass

# With calculations
x = 10
y = 20
max_val = x if x > y else y
print(max_val)  # 20

# With function calls
def is_even(n):
    return "Even" if n % 2 == 0 else "Odd"

print(is_even(7))  # Odd
print(is_even(8))  # Even


# Nested ternary (use sparingly for readability)
score = 85
grade = (("A" if score >= 90 else "B") if score >= 80 else "C" )if score >= 70 else "D" if score >= 60 else "F"
print(grade)  # B

# Better readability with parentheses
grade = (
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
)
print(grade)  # B