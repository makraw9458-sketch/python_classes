## 🟢 EASY SECTION

### Interview Question 1: Variables & Data Types
**Q:** What will be the output of the following code and why?

```python
x = 10
y = x
x = 20
print(x, y)
```

---

### Interview Question 2: Type Conversion
**Q:** What will be the output and why?

```python
result = 10 + 3.5
print(type(result))
print(result)
```


---

### Interview Question 3: Short-Circuit Evaluation
**Q:** What will this code print and why?

```python
r = 0 and 20
print(r)
print(0 and 20)
print(5 or 0)
```


---
---

## 🟡 INTERMEDIATE SECTION


### Interview Question 1: Identity vs Equality
**Q:** Explain the difference between `==` and `is` operators with examples. What will this code output?

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)
print(list1 is list2)
print(list1 is list3)
```


### Interview Question 2: Infinite Loop with Continue
**Q:** What will this code do? Identify the bug.

```python
count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count += 1
```


---

### Interview Question 3: Bitwise Operations
**Q:** Without running the code, what will be the output of these operations? Explain.

```python
a = 0b1010  # 10 in decimal
b = 0b1100  # 12 in decimal

print(a & b)
print(a | b)
print(a ^ b)
```



---
---

## 🔴 HARD SECTION

### Interview Question 1: Ternary Operator Chaining
**Q:** What does this code do? Re-write it using if-elif-else statements. What's the grade for score=85?

```python
score = 85
grade = (
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
)
print(grade)
```


---

### Interview Question 2: List Aliasing
**Q:** What will this code output? Explain the concept.

```python
a = [1, 2, 3]
b = a
c = a[:]

a.append(4)
b.append(5)
c.append(6)

print("a:", a)
print("b:", b)
print("c:", c)
```


---

### Interview Question 3: Loop Control & Scope
**Q:** Analyze this code. What's wrong with it and how would you fix it?

```python
found = False
numbers = [1, 2, 3, 4, 5]
target = 3

for num in numbers:
    if num == target:
        found = True
    break

if found:
    print("Number found!")
```