def ReverseAList(nums):
    Reversed_List = []
    Length = len(nums)

    while Length > 0:
        Reversed_List.append(nums[Length - 1]);
        Length -= 1
    return Reversed_List

numbers = [1,2,3,4,5]
print(ReverseAList(numbers))