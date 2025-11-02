# Palindrome Partitioning | Using Blue Print | DP On Strings | Leetcode 131 | DP

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        t = [[False]*17 for _ in range(17)]
        n = len(s)

        # Palindromes of length 1
        for i in range(n):
            t[i][i] = True
        
        for l in range(2,n+1):
            for i in range(n-l+1):
                j = i + l -1

                if s[i] == s[j]:
                    if l == 2:
                        t[i][j] = True

                    else:
                        t[i][j] = t[i+1][j-1]

        res = []
        currpart=[]

        def solve(index,part,t):
            if index == n:
                res.append(part[:])
                return

            for j in range(index,n):
                if t[index][j] == True:
                    part.append(s[index:j+1]) #do
                    solve(j+1,part,t) #explore
                    part.pop() #undo


        solve(0,currpart,t)

        return res
                



