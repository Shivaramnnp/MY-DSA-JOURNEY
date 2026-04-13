#Find the Average of Numbers
def AverageNo(numbers):
    avg = 0
    for num in numbers:
        avg += num/len(numbers)
    return avg

numbers = [10,20,30,40]
print(AverageNo(numbers))