#Find both the largest and smallest number in a list.
def LargestSmallest(nums):
    largest = max(nums)
    smallest = min(nums)
    print("Largest :",largest)
    print("Smallest :",smallest)
    
nos = [10,12,11,13,14]
print(LargestSmallest(nos))    

