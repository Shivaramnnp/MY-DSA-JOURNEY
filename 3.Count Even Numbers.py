def CountEvenNumber(nums):
    evenNums = nums[0]
    for num in nums:
        if num % 2 == 0 :
            print(num)      

numbers = [1, 2, 3, 4, 5, 6]
CountEvenNumber(numbers)