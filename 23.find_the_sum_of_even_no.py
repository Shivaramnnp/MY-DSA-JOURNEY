#find the sum of even no 
def SumOfEven(nums):
    sum = 0
    for num in nums:
        if  num % 2 == 0:
         sum += num
    return sum
numbers = [12,22,12,13]
print(SumOfEven(numbers))