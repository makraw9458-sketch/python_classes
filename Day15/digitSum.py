def sum_of_digits(num):
    sum = 0

    while num > 0:
        # add last digit to sum
        sum += num%10
        # remove the last digit from num
        num = int(num/10)

    return sum



a =123
print(sum_of_digits(a))
print(sum_of_digits(122345))