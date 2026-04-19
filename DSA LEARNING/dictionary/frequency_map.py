def freq_map(nums):

    freq_map = dict()
    for i in range(len(nums)):
        if nums[i] in freq_map:
            freq_map[nums[i]] += 1
        else:
            freq_map[nums[i]] = 1
            
    return  freq_map
nos = [11,11,11,11,11,12,11,12,12,11,12,12,12]
print(freq_map(nos))

#TC = O(n)
#SC = 0(n)


def hash_map(nums):

   hash_map = {}
   n = len(nums)
   for i in range(0,n):
       hash_map[nums[i]] = hash_map.get(nums[i],0)+1
   return hash_map
print(hash_map(nos))