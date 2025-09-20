class Solution:
    def countSubstrings(self, s: str) -> int:
        #Recursion And Memoization(Brute Force)
        '''
        n = len(s)

        dp = [[None]*(n+1) for _ in range(n+1)]

        def check(i,j):
            if i > j:
                return True

            if dp[i][j] is not None:
                return dp[i][j]

            if s[i] == s[j]:
                dp[i][j] = check(i+1,j-1)
                return dp[i][j]

            dp[i][j]= False
            return dp[i][j]

        count = 0
        for i in range(n):
            for j in range(i,n):
                if check(i,j):
                    count += 1

        return count

        '''

        #Bottom Up Approach(Optimized Approach)
        '''
        State Definition: True --> t[i][j] --> s[i][j] is a Palindrome. 
                          False --> t[i][j] --> s[i][j] is not a Palindrome.

        Palindrome DP Problems Blueprint:

        - t[i][i] = True (Always)  [Single Length]
        - i+1 == j ---> t[i][j] = (s[i] == s[j]) [2 Length String]
        - if Generic Length > 2:

            - Check for s[i] and s[j] if s[i] == s[j]
            - Get Ans of s[i+1] and s[j-1] if it is Palindrome or not.
            - Means s[i] == s[j] and t[i+1][j-1] then t[i][j] = True

        '''

        n = len(s)

        t = [[False]*(n) for _ in range(n)]

        count = 0

        for l in range(1,n+1):
            for i in range(0, n - l +1):
                j = i + l -1

                if i == j: # Case 1: len == 1
                    t[i][j] = True

                elif i+1 ==j: # Case 2: len == 2
                    t[i][j] = (s[i] == s[j])

                else: # Case 3: len > 2(Generic)
                    t[i][j] = (s[i] == s[j] and t[i+1][j-1])

                if t[i][j] : # Increase Count
                    count += 1

        return count
