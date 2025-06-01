class Solution:
    import heapq
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans = 0
        hired = 0

        i = 0
        j= len(costs)-1

        pq1= []
        pq2 = []

        while hired < k:
            while len(pq1)<candidates and i <= j:
                heapq.heappush(pq1,costs[i])
                i +=1

            while len(pq2)<candidates and j>=i:
                heapq.heappush(pq2,costs[j])
                j -=1

            top1 = pq1[0] if pq1 else float('inf')
            top2 = pq2[0] if pq2 else float('inf')

            if top1 <= top2:
                ans += heapq.heappop(pq1)
            else:
                ans += heapq.heappop(pq2)
            
            hired+=1

        return ans

            
'''
 Approach:
	1.	Two Pointers + Two Min-Heaps:
        •	Use two heaps:
        •	pq1: heap of costs from the left side.
        •	pq2: heap of costs from the right side.
        •	Use two pointers:
        •	i: starts from left (index 0)
        •	j: starts from right (index len(costs) - 1)
	2.	Initialize Heaps:
        •	While pq1 has fewer than candidates and i <= j, push costs[i] into pq1 and move i right.
        •	While pq2 has fewer than candidates and j >= i, push costs[j] into pq2 and move j left.
	3.	Hire Workers (k times):
        •	Peek the top values (minimum) of both heaps.
        •	Choose the smaller one:
        •	If pq1 is smaller or equal, pop from pq1.
        •	Else, pop from pq2.
        •	Add that cost to the total (ans) and increment hired.
	4.	Repeat until k workers are hired.

    •	Time Complexity:
        •	Each heap operation is O(log c) where c = candidates
        •	For k workers: O(k log c)
        •	So overall: O(k log candidates)
	•	Space Complexity:
        •	pq1 and pq2 hold at most candidates items each
        •	So: O(candidates)

'''