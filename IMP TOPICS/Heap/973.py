class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        ans = []
        heap = []

        for point in points:
            x1 , y1 = 0,0
            x2, y2 = point

            val = (x2 - x1)**2 + (y2 - y1)**2

            ans.append([val,x2,y2])

        for point in ans:
            heapq.heappush(heap, (-point[0],point[1],point[2]))

            if len(heap) > k:
                heapq.heappop(heap)

        
        return [[x,y] for _,x,y in heap]

        '''

        heap = []

        for x, y in points:
            dist = x*x + y*y

            heapq.heappush(heap,(-dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)


        return [[x, y] for _, x, y in heap]

        
            