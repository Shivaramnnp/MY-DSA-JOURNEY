def most_frequent(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    max_count = 0
    result = None
    for num in freq:
        if freq[num] > max_count:
            max_count = freq[num]
            result = num
    return result


numbers = [1, 2, 2, 3, 3, 3, 4]
print(most_frequent(numbers))