#Minimum Insertion Steps to Make a String Palindrome | Blue Print | DP On Strings | Leetcode 1312



class Solution:
    def minInsertions(self, s: str) -> int:
        # Top Down Memoization
        '''
        n = len(s)
        dp = [[-1]*n for _ in range(n)]
        def solve(idx1, idx2):
            if idx1> idx2:
                return 0

            if dp[idx1][idx2] != -1:
                return dp[idx1][idx2]

            if s[idx1] == s[idx2]:
                return solve(idx1+1, idx2-1)

            take = 1+ solve(idx1,idx2-1)
            nottake = 1 + solve(idx1+1,idx2)

            dp[idx1][idx2] = min(take,nottake)

            return dp[idx1][idx2]
    

        return solve(0,n-1)

        '''

        #Bottom up Approach Using #647 Blueprint

        t = [[0]*501 for _ in range(501)]
        n = len(s)

        for l in range(2,n+1):
            for i in range(0,n-l+1):
                j = i+l-1
                if s[i] == s[j]:
                    t[i][j] = t[i+1][j-1]

                else:
                    t[i][j] = 1 + min(t[i][j-1],t[i+1][j])

        return t[0][n-1]


        #TC : O(n*n)
        #SC : O(n*n)

