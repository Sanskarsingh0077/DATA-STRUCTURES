class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxheap = []

        res = ''

        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heapq.heappush(maxheap, (count, char))


        while maxheap:
            count, char = heapq.heappop(maxheap)

            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxheap:
                    break

                count2 , char2 = heapq.heappop(maxheap)
                res += char2
                count2 += 1

                if count2:
                    heapq.heappush(maxheap, (count2, char2))
            else:

                res += char
                count += 1

            if count:
                heapq.heappush(maxheap, (count, char))


        return res







