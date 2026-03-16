class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])

        # Idea: Get all the rhombus and maintain sums in a maxheap then return top three elements

        sums = set()

        for i in range(rows):
            for j in range(cols):

                # size 0 rhombus
                sums.add(grid[i][j])

                k = 1
                while True:
                    if i-k < 0 or i+k >= rows or j-k < 0 or j+k >= cols: #Boundary
                        break

                    total = 0

                    # four edges
                    for d in range(k):
                        total += grid[i-k+d][j+d]   # top → right
                        total += grid[i+d][j+k-d]   # right → bottom
                        total += grid[i+k-d][j-d]   # bottom → left
                        total += grid[i-d][j-k+d]   # left → top

                    sums.add(total)
                    k += 1

        heap = []
        for x in sums:
            heapq.heappush(heap, x)

            if len(heap) > 3:
                heapq.heappop(heap)

        res = sorted(heap, reverse=True)

        return res
        

        

            



