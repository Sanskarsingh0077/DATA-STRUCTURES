class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        opr = 0
        i = 0
        count1 = 0

        while i < n:
            if s[i] == '0':
                opr += count1
                while i < n and s[i] == '0':
                    i += 1

            else:
                count1 += 1
                i += 1
 
        return opr
