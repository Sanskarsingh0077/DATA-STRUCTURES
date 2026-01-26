
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Bucket Sort ---> O(n)

        n = len(nums)

        #Creating the freq Map
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1

            else:
                freq[num] = 1

        #Create Buckets

        buckets = [[] for _ in range(n+1)]

        #fill buckets

        for num, count in freq.items():
            buckets[count].append(num)

        res = []
        #Accessing buckets and getting max freq nums == k

        for f in range(len(buckets)- 1 , 0, -1):
            for num in buckets[f]:
                res.append(num)

            if len(res) == k:
                return res






        

