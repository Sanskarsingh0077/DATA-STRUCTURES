class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right= 0
        left = 0

        seen =set()
        max_len= 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1

            seen.add(s[right])

            max_len= max(max_len,right-left+1)

        return max_len

        '''
        Approach: Sliding Window (Two Pointer)
        1.	Initialize:
        •	left = 0 (start of the window)
        •	right = 0 (end of the window)
        •	seen = set() to track characters in the current window
        •	max_len = 0
        2.	Move the right pointer:
        •	If s[right] is not in seen:
        •	Add it to seen
        •	Update max_len as max(max_len, right - left + 1)
        •	Move right forward
        •	If s[right] is in seen:
        •	Remove s[left] from seen
        •	Move left forward
        3.	Repeat until right reaches end of string.

        Time Complexity: O(n)
        Space Complexity : O(n)

        '''