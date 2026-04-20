def first_non_repeating(numbers):
    freq = {}

   
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num in numbers:
        if freq[num] == 1:
            return num

    return None


numbers = [4, 5, 1, 2, 1, 2]

result = first_non_repeating(numbers)

if result is not None:
    print("First non-repeating element:", result)
else:
    print("No non-repeating element found")