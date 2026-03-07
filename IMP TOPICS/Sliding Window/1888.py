class Solution:
    def minFlips(self, s: str) -> int:
        k = len(s)
        strng = s + s
        left = 0

        s1 = ''.join(str(i%2) for i in range(len(strng)))
        s2 = ''.join(str((i+1)%2) for i in range(len(strng)))

        flips = float('inf')
        diff1 = 0
        diff2 = 0
        

        for i in range(len(strng)):
            # Add new Element to window
            if strng[i] != s1[i]:
                diff1 += 1

            if strng[i] != s2[i]:
                diff2 += 1

            # Window becomes bigger than K(Shrinking)
            if i >= k:
                if strng[left] != s1[left]:
                    diff1 -= 1

                if strng[left] != s2[left]:
                    diff2 -= 1


                left += 1
            # Window becomes == K 
            if i >= k-1:
                flips = min(flips, diff1, diff2)

        return flips

                

