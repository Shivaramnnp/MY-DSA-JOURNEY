def are_anagrams(list1, list2):
    if len(list1) != len(list2):
        return False

    freq1 = {}
    freq2 = {}

    # Count frequency for list1
    for num in list1:
        if num in freq1:
            freq1[num] += 1
        else:
            freq1[num] = 1

    # Count frequency for list2
    for num in list2:
        if num in freq2:
            freq2[num] += 1
        else:
            freq2[num] = 1

    return freq1 == freq2


list1 = [1, 2, 2, 3]
list2 = [2, 3, 2, 1]

if are_anagrams(list1, list2):
    print("Anagrams")
else:
    print("Not Anagrams")
