class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        #Brute Force
        for i in range(0, len(nums) - 1):
            for j in range(1, len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    return [i,j]
        '''


        

        seen = {}

        for index, num in enumerate(nums):
            complement = target -num
            if complement in seen:
                return [seen[complement],index]
            
            seen[num] = index
        