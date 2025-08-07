#House Robber 2 (LEETCODE # 213)
class Solution:

    def rob(self, nums: List[int]) -> int:
        # Bottom - up Space O(1):
        
        n = len(nums)

        if n == 1:
            return nums[0]

        def solve(houses):
            prev = 0
            prevprev = 0
            for money in houses:
                
                take = money + prevprev
                skip = prev

                curr = max(skip,take)

                prevprev = prev
                prev = curr

            return prev

        take_first = solve(nums[:-1]) # Rob from 0 to n-2
        take_last = solve(nums[1:]) # Rob from 1 to n-1

        return max(take_first,take_last)



        # Bottom Up Approach :
        '''
        n = len(nums)

        if n == 1:
            return nums[0]
            
        # Case-1 (Take from 1st House - Hence skip the last house)
        t = [0]*(n+1)
    
        for i in range(1,n): # First loop should go from 1 to n (exclusive), which means range(1, n)
            take = nums[i-1] + (t[i-2] if i-2 >=0 else 0)
            skip = t[i-1]

            t[i] = max(take,skip)

        result_1 = t[n-1]

        # Case-2 (Take from 2nd House - Hence take the last house)
        t = [0]*(n+1)
        t[1] = 0

        for i in range(2,n+1) #Second loop should go from 2 to n + 1 (inclusive of n-1 index)
            take = nums[i-1] + (t[i-2] if i-2 >=0 else 0)
            skip = t[i-1]

            t[i] = max(take,skip)

        result_2 = t[n]

        return max(result_1,result_2)

        '''


        # Memoization
        '''
        def solve(index,n): #Same as House Robber 1
            if index > n:
                return 0
            
            if dp[index] != -1:
                return dp[index]
                
            pick = nums[index]+ solve(index+2,n)
            skip = solve(index+1,n)

            dp[index] = max(pick,skip)
            return dp[index]

        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0],nums[1])

        dp = [-1]*(n+1)
        take_0th_index = solve(0,n-2) # Case 1 : taking first house so last is not valid
        dp = [-1]*(n+1)
        take_1st_index = solve(1,n-1) # Case 2 : taking second house so last house is valid

        return max(take_0th_index,take_1st_index)
        '''
       


        



