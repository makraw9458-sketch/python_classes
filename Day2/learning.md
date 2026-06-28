# To Learn
1. Keywords in py
    [
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
    ]

2. assigning values to variables and basic arithmetic operations.

3. operators/operands and their types
    - Arithmetic operators - [+, - , *, /, %(remainder), **]
    - Relational/ Comparison - [==, !=, >, <, >=, <=]
    - Assignment operator - [=, +=, -= , *=, /=, %=, **=]
    - Logical operators - [and, or, not]
4. Type conversion(interpreter) and type casting(manual) and the concept of superior data types(like float is superior then int, hence on addition int is converted to float)
    - functions to type cast [int(), float(), ]

5. the input() function and type casting input value.

# Activities
1. install and setup git and github and push first code
    - install git
    - run commands
    git config --global user.name "user name"
    git config --global user.email "email "
    git config --global --list

# Practice
1. WAP to create 2 int variables a & b and print true if a is greater else print false.
2. WAP to input the height and width of a rectangle and calculate its area.
3. WAP to print average of 5 numbers.


# queries
1. why this program prints 20 not True
    r = 10 and 20
    print(r)

    because of short circuiting
    - In Python, the and operator evaluates from left to right and returns the first falsy value it encounters. If it finds a False (or any falsy value like 0, None, "", []), it short-circuits immediately and returns that falsy value — because once one operand is false, the entire expression is false, and the rest doesn't matter.

    - The or operator evaluates from left to right and returns the first truthy value it encounters. If it finds a True (or any truthy value), it short-circuits immediately and returns that value — because once one operand is true, the entire expression is true, and the rest doesn't matter.
    