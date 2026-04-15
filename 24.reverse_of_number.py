#reverse of the number
def reverse_of_number(nums):
    length = len(nums)
    reversed_list = []
    while length > 0:
        reversed_list.append(nums[length - 1])
        length -= 1
    return reversed_list

    

nos =[12,11,13,14]
print(reverse_of_number(nos))
