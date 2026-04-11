def LinearSearch(numbers, target):
    for i in range(len(numbers)):

        if numbers[i] == target:
            print(numbers[i],"Found at Index",i )
            return 
    print("Not Found!")

numbers = [5, 8, 12, 7, 3]
target = 7
LinearSearch(numbers, target)