class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
       
        def findtopelement(mp, ele):
            pq = []
            for key, freq in mp.items():
                heapq.heappush(pq,(freq,key))

                if len(pq) > x:
                    heapq.heappop(pq)

            total = 0
            while pq:
                freq,key = heappop(pq)
                total += freq * key

            return total

        freq = {}
        res = []
        
        i = 0
        j = 0
        while j < n: # Sliding Window
            freq[nums[j]] = freq.get(nums[j], 0) + 1

            if j -i +1 == k:
                res.append(findtopelement(freq,x))
                
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    freq.pop(nums[i])

                i += 1

            j += 1

        return res

            




            


