#Count How Many Times a Number Appears

def CountNumber(nums , target):
    count = 0

    for num in nums:
        if num == target:
         count +=1
    return count

numbers = [2, 3, 2, 4, 2]
target = 2
print(CountNumber(numbers, target))