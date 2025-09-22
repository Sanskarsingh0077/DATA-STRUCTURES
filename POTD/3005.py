def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1


        max_val = max(freq.values())

        total = 0

        for v in freq.values():
            if v == max_val:
                total += v

        return total