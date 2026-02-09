class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts1 , counts2 = [0] * 26 , [0] * 26

        # storing data in arrays
        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] += 1
            counts2[ord(s2[i]) - ord('a')] += 1

        if counts1 == counts2:
            return True

        # Sliding Window of Size len(s1) 

        for r in range(len(s1), len(s2)):
            counts2[ord(s2[r]) - ord('a')] += 1 # add new element in right
            counts2[ord(s2[r - len(s1)]) - ord('a')] -= 1  # delete old from left

            if counts1 == counts2:
                return True

        return False


            

            
