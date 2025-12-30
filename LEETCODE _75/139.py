class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1]*n
        def solve(idx):
            if idx == n:
                return True

            if s in wordDict:
                return True

            if dp[idx] != -1:
                return dp[idx]

            for l in range(1,n+1):
                temp = s[idx:idx+l]

                if temp in wordDict and solve(idx+l):
                    dp[idx] = True
                    return dp[idx]

            
            dp[idx] = False
            return dp[idx]


        return solve(0)

        #TC : O(n * 2^n)