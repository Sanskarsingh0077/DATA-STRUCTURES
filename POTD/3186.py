class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # Step 1: Count frequency
        map_val = {}
        for x in power:
            if x not in map_val:
                map_val[x] = 0
            map_val[x] += 1

        # Step 2: Sort unique powers
        nums = sorted(map_val.keys())
        n = len(nums)

        # Step 3: DP with memoization
        '''
        dp = [-1]*n

        def solve(idx):
            if idx >= n:
                return 0

            if dp[idx] != -1:
                return dp[idx]

            skip = solve(idx+1) # Option 1: Skip current power

            # Option 2: Take current power and skip next 2 adjacent powers (x+1 and x+2)
            j = bisect.bisect_left(nums, nums[idx] + 3, idx + 1)

            take = nums[idx] * map_val[nums[idx]] + solve(j)

            dp[idx]= max(skip, take)
            return dp[idx]

        return solve(0)

        '''

        #Bottom up
        # t[i] = max total damage if we start from idx i

        t = [0]*(n+1)
        result = float('-inf')

        for i in range(n-1, -1, -1):
            j = bisect.bisect_left(nums, nums[i] + 3, i + 1)

            
            skip = t[i+1]
            take = nums[i] * map_val[nums[i]] + t[j]

            t[i] = max(skip, take)

            result = max(result, t[i])

        return result