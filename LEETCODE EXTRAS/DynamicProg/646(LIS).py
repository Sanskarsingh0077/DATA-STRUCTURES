class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Top Down Memoization LIS Variant

        '''
        pairs.sort(key=lambda x:x[1]) # sort array for second element
        n = len(pairs)

        dp = [[-1]*(n+1) for _ in range(n+1)]
        
        def solve(index,prev):
            if index >= n:
                return 0

            if dp[index][prev] != -1:
                return dp[index][prev]

            take = 0
            if pairs[index][0]>pairs[prev][1] or prev == -1: #condition for taking
                take = 1 + solve(index+1,index)

            skip = solve(index+1,prev) 
            
            if prev != -1:

                dp[index][prev] =  max(skip,take)
                return dp[index][prev]
            
            return max(take,skip)

        
        return solve(0,-1)
        '''

        #Bottom Up
        pairs.sort(key=lambda x:x[1])
        n = len(pairs)
        t = [1]*(n)
        maxLIS = 1

        for i in range(0,n):
            for j in range(0,i):
                if pairs[j][1] < pairs[i][0]:
                    t[i] = max(t[i],t[j]+1)
                    maxLIS = max(maxLIS,t[i])

        return maxLIS
