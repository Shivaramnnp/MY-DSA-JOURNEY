#Count how many numbers are even and how many are odd.
def EvenOddCount(nums):
    even = 0
    for num in nums:
        if num % 2 == 0 :
            even += 1
    odd = len(nums) - even
    print("Even :",even)
    print("Odd :",odd)
    return "code exected"
    

nos = [12,13,14,11,1]
print(EvenOddCount(nos))


