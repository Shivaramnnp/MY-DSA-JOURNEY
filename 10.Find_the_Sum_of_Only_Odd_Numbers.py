#Find the Sum of Only Odd Numbers
def SumOfOdd(numbers):
    sum = 0

    for num in numbers:
        if num % 2 != 0:
            sum += num

    return sum

numbers =[1, 2, 3, 4, 5]
print(SumOfOdd(numbers))

            