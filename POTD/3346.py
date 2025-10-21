class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maxele = max(nums)+k

        freq = [0]*(maxele+1)

        for num in nums:
            freq[num] += 1

        #cumulative sum
        for i in range(1,maxele+1):
            freq[i] += freq[i-1]

        result = 0

        for target in range(maxele+1):
            if freq[target] == 0:
                continue

            leftNum = max(0, target - k)
            rightNum = min(maxele, target + k)

            totalcount = freq[rightNum] - (freq[leftNum - 1] if leftNum > 0 else 0)

            targetcount = freq[target] - (freq[target-1] if target >0 else 0)

            needConversion = totalcount - targetcount
            
            maxPossibleFreq = targetcount + min(needConversion, numOperations)

            result = max(result, maxPossibleFreq)
        
        return result