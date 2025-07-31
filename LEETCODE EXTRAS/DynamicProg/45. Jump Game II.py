class Solution:
    def jump(self, nums: List[int]) -> int:
        #Top Down Memoization
        '''
        n = len(nums)
        dp = [-1]*n

        def solve(index):
            if index >= n-1:
                return 0

            mini = float('inf')

            if dp[index] != -1:
                return dp[index]

            for i in range(1, nums[index]+1):
                mini = min(mini, 1 + solve(index + i))

            dp[index] = mini
            return dp[index]

        return solve(0)

        '''

        # Greedy Solution
        '''
        n = len(nums)
        farthest = 0
        curr_end = 0
        jumps = 0


        for i in range(n-1):
            farthest = max(farthest, i + nums[i])

            if i == curr_end:
                jumps += 1

                curr_end = farthest

        return jumps

        '''

        #Another Way

        jumps = 0
        l = 0
        r = 0

        while r < len(nums) - 1:
            farthest = 0

            for i in range(l,r+1):
                farthest = max( i+ nums[i] , farthest)
            
            l = r+1
            r = farthest
            jumps += 1

        return jumps
