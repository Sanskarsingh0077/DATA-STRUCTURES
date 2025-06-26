class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Top Down memoization Approach
        '''
        dp = [[-1]*2 for i in range(len(nums)+1)]

        def solve(index,flag):
            if index >= len(nums):
                return 0

            if dp[index][int(flag)] != -1:
                return dp[index][int(flag)]
            
            skip = solve(index+1,flag)

            val = nums[index]

            if flag is False: # Odd / Even Case
                val = - val
            
            take = solve(index+1, not flag) + val


            dp[index][flag] =  max(take,skip)
            return dp[index][int(flag)]

        
        return solve(0,True)
        '''


        #Bottom Up Approach:
        '''
        n = len(nums)

        dp = [[0]*2 for i in range(n+1)]

        for i in range(1,n+1):

            dp[i][0] = max(dp[i-1][1]+ nums[i-1], dp[i-1][0]) #For odd Case

            dp[i][1] = max(dp[i-1][0]-nums[i-1], dp[i-1][1]) # For even Case

        return max(dp[n][0],dp[n][1])
        '''


        #Bottom Up Space Optimized:

        even = 0
        odd = 0
        for num in nums:
            even = max(even, odd + num)
            odd = max(odd, even - num)
        return max(even,odd)


'''
Comments:

dp[i][odd] = max(dp[i-1][even] + nums[i-1], dp[i-1][odd])
dp[i][even] = max( dp[i-1][odd] - nums[i-1], dp[i-1][even])

Time Complexity : O(n)
Space Complexity : O(n)

'''
        