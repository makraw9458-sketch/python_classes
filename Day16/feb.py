# addition of last 2 nums

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

#  13 = 8th == 7th + 6th
# nth = (nth-1) + (nth-2)

def feb(n):
    # base case
    if(n == 0 or n == 1):
        return n

    return feb(n-1) + feb(n-2)


print(feb(8))