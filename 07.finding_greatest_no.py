#Find How Many Numbers Are Greater Than a Given Number
def GreatestNoFinder(nums , target):
    count = 0

    for num in nums:
        if num > target:
            count+=1
    return count

numbers =[1,2,3,4,5,6]
target = 2
print(GreatestNoFinder(numbers, target))

        