class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x):
            rev = 0
            while x:
                rev = rev * 10 + x % 10
                x //= 10
            return rev

        mp = {}
        res = float('inf')

        for i, num in enumerate(nums):
            rev_num = reverse(num)

            if num in mp: # Condition Met mirror pair found
                res = min(res, i - mp[num])

            mp[rev_num] = i # Update rev num index in map

        return res if res != float('inf') else -1

        
        
        

