class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')]*n
        prices[src] = 0

        # Bellman Ford
        for i in range(k+1):

            temp = prices.copy()

            for s, d , c in flights:
                if prices[s] == float('inf'):
                    continue

                if prices[s] + c < temp[d]:
                    temp[d] = prices[s] + c


            prices = temp

        return -1 if prices[dst] == float('inf') else prices[dst]