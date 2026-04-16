#Count Occurrences in Sorted Array
def count(nums, target):
    count = 0
    for num in nums:
        if num == target:
            count += 1
    return count

nums = [12,11,13,11,11,11]
target = 11
print(count(nums , target))
    