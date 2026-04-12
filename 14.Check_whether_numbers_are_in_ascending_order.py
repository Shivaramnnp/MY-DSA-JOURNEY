# 

def AscendingOrder(nums):

    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return "LIST IS NOT SORTED"

    return"LIST IS SORTED"    

numbers = [1,2,3,4,5]
print(AscendingOrder(numbers))

number = [1,2,3,4,5,1]
print(AscendingOrder(number))