class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)


        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if first == second:
                continue

            else:
                new = abs(first - second)
                heapq.heappush(heap, -new)

        return -heap[0] if heap else 0

 
