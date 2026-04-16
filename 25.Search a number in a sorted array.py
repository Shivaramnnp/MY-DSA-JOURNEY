#Search a number in a sorted array.
def SearchNumber(nums, target):
    for num in nums:
        if num == target:
            return nums.index(num)

nums = [11,12,12,13,14]
target = 13
print(SearchNumber(nums, target))