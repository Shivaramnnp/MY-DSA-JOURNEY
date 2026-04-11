def largest (nums):
    largest = nums[0]
    
    for num in nums:
        if num > largest:
            largest = num

    return largest

numbers = [1, 10 , 9, 8 , 11]

print(largest(numbers))