class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = {}
   
        for i, ch in enumerate(s): # Store last index of appearence of each element # O(n)
            freq[ch] = i

        size ,end = 0, 0
        ans = []
 
        for i, ch in enumerate(s):  # O(n)
            size += 1
            end = max(end, freq[ch]) #update end if end < freq[ch]

            if i == end: # if end == i , add to ans
                ans.append(size)
                size = 0 # reset size

        return ans

