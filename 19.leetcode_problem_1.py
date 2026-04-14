
def twoSum( nums, target):
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i
number = [12,10,11,13,14]
target = 23
print(twoSum(number,target))
        