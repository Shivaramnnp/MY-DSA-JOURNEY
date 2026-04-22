def find_duplicates(nums):

    freq = {}
    result = []

    # Step 1: Count frequency
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Step 2: Collect duplicates
    for num in freq:
        if freq[num] > 1:
            result.append(num)

    return result


numbers = [1, 2, 3, 2, 4, 5, 1]
print(find_duplicates(numbers))