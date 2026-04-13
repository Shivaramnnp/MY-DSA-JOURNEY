#Count how many numbers are greater than a given number.
def CountGreater(numbers, target):
    count = 0
    for num in numbers:
        if target < num:
         count +=1
    return count 

numbers = [10,20,30,40]
target = 10
print(CountGreater(numbers , target))
