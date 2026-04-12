#Find the Maximum Difference
def MaxDif(numbers):
    for num in numbers:
        dif = max(numbers) - min(numbers)
    print(dif)

numbers =[1,2,3,4,12]
MaxDif(numbers)