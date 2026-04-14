#Check whether a number exists in the list.
def NumExists(nums, target):
    for num in nums:
        if num == target:
            return("Number Existed!")
        else:
            return("Number Not Found!")

nums = [12,11,13,14,15]
target = 18
print(NumExists(nums , target))