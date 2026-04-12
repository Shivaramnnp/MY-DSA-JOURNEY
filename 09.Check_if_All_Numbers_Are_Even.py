#Check if All Numbers Are Even
def evenNo(numbers):
    for num in numbers:
        if num % 2 != 0:
            return "not all nos are even"
    return "all are even"

numbers = [6,4,6,8]
print(evenNo(numbers))

