#Find the Difference Between First and Last Element

def Difference(numbers):
    sub = 0
    sub = numbers[-1] - numbers[0]
    return sub

numbers = [10 , 20 , 30 , 40]
print(Difference(numbers))