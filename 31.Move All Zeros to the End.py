def move_zeros(nums):

    result = []

    # Step 1: Add non-zero numbers
    for num in nums:
        if num != 0:
            result.append(num)

    # Step 2: Count zeros
    zeros = len(nums) - len(result)

    # Step 3: Add zeros at the end
    for _ in range(zeros):
        result.append(0)

    return result


numbers = [0, 1, 0, 3, 12]
print(move_zeros(numbers))