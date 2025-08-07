class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        n= len(words)

        

        def predecessorcheck(word1,word2):
            m = len(word1)
            n = len(word2)
            if m >= n or n - m != 1:
                return False

            i = 0
            j = 0

            while(i< m and j< n):
                if word1[i] == word2[j]:
                    i +=1
                j+=1

            return i == m


        '''
        dp = [[-1]*(n+1) for _ in range(n+1)]
        def solve(index,prev):

            if index == n:
                return 0

            if dp[prev+1][index] != -1:
                return dp[prev+1][index]


            take = 0
            if prev == -1 or predecessorcheck(words[prev],words[index]):
                take = 1 + solve(index+1,index)


            skip = solve(index+1,prev)


            dp[prev+1][index] = max(skip,take)
            return dp[prev+1][index]

        return solve(0,-1)

        '''
        # Bottom Up

        t = [1]*(n)
        maxLIS = 1

        for i in range(n):
            for j in range(i):
                if predecessorcheck(words[j],words[i]):
                    t[i] = max(t[i],t[j]+1)
                    maxLIS = max(maxLIS,t[i])

        return maxLIS

        #Optimal Solution

        