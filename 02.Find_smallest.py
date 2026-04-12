def FindSmallest (nums):
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
    return smallest
numbers = [13, 14, 12, 122, 11]       
print(FindSmallest(numbers))
   