#1092. Shortest Common Supersequence 

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        t = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    t[i][j] = i+j
                    
                elif str1[i-1] == str2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]

                else:
                    t[i][j] = 1 + min(t[i-1][j],t[i][j-1])

        
        i = m
        j = n
        res = []

        while i>0 and j>0:
            if str1[i-1] == str2[j-1]:
                res.append(str1[i-1])
                i -= 1
                j -= 1

            else:
                if t[i-1][j] < t[i][j-1]:
                    res.append(str1[i-1])
                    i -= 1

                else:
                    res.append(str2[j-1])
                    j -= 1

        while i > 0:
            res.append(str1[i-1])
            i -= 1

        while j > 0 :
            res.append(str2[j-1])
            j -= 1

        res.reverse()

        return "".join(res)