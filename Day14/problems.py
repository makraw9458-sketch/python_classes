# problem 1 : wap to find the avg of 5 numbers
def myAvg(nums):
    n = len(nums)
    result = sum(nums)/n
    return result

lis = [1,2,3,4,5,6]
avg = myAvg(lis)
print(f"average of {lis} is {avg}")