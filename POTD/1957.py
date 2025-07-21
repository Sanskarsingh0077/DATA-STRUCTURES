class Solution:
    def makeFancyString(self, s: str) -> str:
        out=""
        freq = 1

        out += s[0]
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                freq +=1
            else:
                freq = 1

            if freq <= 2:
                out += s[i]

        return out