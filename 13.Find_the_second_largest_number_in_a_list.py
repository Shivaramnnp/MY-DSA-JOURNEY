#Find the second largest number in a list.
def SecoundLargest(nums):
   Sorted_Nums = sorted(nums, reverse = True)

   return Sorted_Nums[1]
   
numbers = [1,2,3,4,5]
print(SecoundLargest(numbers))