#Find How Many Times a Number Appears
def TimesANumber(nums, target):
    count = 0
    for num in nums:
        if num == target:
            count +=1
    return count
Nos = [1,2,1,2,1,2,11]
target = 11
print(TimesANumber(Nos, target))
