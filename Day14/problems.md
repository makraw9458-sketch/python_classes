Here are 5 intermediate function practice problems in Python (no recursion):

---

## Problem 1: **Multiples Finder**
Write a function `find_multiples(num, limit)` that returns a list of all multiples of `num` from 1 up to (but not including) `limit`.

**Example:**
```python
find_multiples(3, 20)  # Returns: [3, 6, 9, 12, 15, 18]
find_multiples(5, 30)  # Returns: [5, 10, 15, 20, 25]
```

---

## Problem 2: **Digit Sum Calculator**
Write a function `sum_of_digits(n)` that takes a positive integer `n` and returns the sum of its digits. Do NOT convert the number to a string. Use arithmetic operations instead.

**Example:**
```python
sum_of_digits(1234)   # Returns: 10 (1+2+3+4)
sum_of_digits(999)    # Returns: 27 (9+9+9)
sum_of_digits(7)      # Returns: 7
```

---

## Problem 3: **Prime Number Checker**
Write a function `is_prime(n)` that returns `True` if `n` is a prime number and `False` otherwise. Handle edge cases like negative numbers, 0, and 1.

**Example:**
```python
is_prime(17)    # Returns: True
is_prime(1)     # Returns: False
is_prime(2)     # Returns: True
is_prime(15)    # Returns: False
```

---

## Problem 4: **Character Frequency Counter**
Write a function `char_frequency(text)` that takes a string and returns a dictionary with the count of each character (case-insensitive). Count only alphabetic characters (a-z).

**Example:**
```python
char_frequency("Hello World")  
# Returns: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

char_frequency("Python")
# Returns: {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
```

---

## Problem 5: **GCD Calculator**
Write a function `gcd(a, b)` that finds the Greatest Common Divisor of two positive integers using the **Euclidean algorithm** (subtraction method or modulo method — your choice, but no recursion). The GCD is the largest number that divides both `a` and `b` without leaving a remainder.

**Example:**
```python
gcd(48, 18)   # Returns: 6
gcd(100, 75)  # Returns: 25
gcd(17, 13)   # Returns: 1
```

---

## Bonus Challenge (Optional)
After solving these, try to combine them:
- Write a function `find_prime_digit_sums(start, end)` that returns a list of numbers between `start` and `end` whose digit sum is a prime number. Use your functions from Problems 2 and 3.