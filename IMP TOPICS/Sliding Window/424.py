class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        count = {}

        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]] = 0

            count[s[right]] += 1

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res

        






        

