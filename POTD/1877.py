#Core Logic: Sorting + Two Pointer


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort() # n logn 
        i = 0 
        j = n-1

        pair = 0

        while i < j: #O(n)
            pair = max(pair,nums[i] + nums[j])

            i +=1
            j -= 1

        return pair

        # TC : O( N LogN) ---> sorting
        # SC : O(1) ---> No extra space


        
