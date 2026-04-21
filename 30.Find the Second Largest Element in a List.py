def second_largest(nums):

    if len(nums) < 2:
        return "No second largest element"

    largest = float('-inf')
    second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num

        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        return "No second largest element"

    return second


numbers = [10, 20, 4, 45, 99]
print(second_largest(numbers))