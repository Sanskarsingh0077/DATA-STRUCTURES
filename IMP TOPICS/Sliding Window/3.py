class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() #Create Set to Store char
        left = 0 # Left Pointer

        res = 0

        for right in range(len(s)): # Right Pointer 
            while s[right] in charSet: # check if new char in set if yes remove left shrink window
                charSet.remove(s[left])
                left += 1


            charSet.add(s[right]) # add element to window and extend window
            res = max(res, right - left + 1) #update size

        return res