def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums) #3*n

        n = N // 3

        leftminsum = [0]*N #Create Arrays
        rightmaxsum = [0]*N

        maxheap = []
        leftsum = 0

        for i in range(0,2*n):
            heapq.heappush(maxheap, -nums[i])
            leftsum += nums[i]

            if len(maxheap) > n:
                leftsum += heapq.heappop(maxheap)
                
            leftminsum[i] = leftsum

        minheap = []
        rightsum = 0

        for i in range(N-1,n-1,-1):
            heapq.heappush(minheap, nums[i])
            rightsum += nums[i]

            if len(minheap) > n:
                rightsum -= heapq.heappop(minheap)

            rightmaxsum[i] = rightsum


        result = float('inf')

        for i in range(n-1, 2*n):
            result = min(result, leftminsum[i] - rightmaxsum[i+1])


        return result