class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: #Early Check
            return False

        #Creat Freq map ---> O(n)

        freq = {}
        for i in hand:
            if i not in freq:
                freq[i] = 0

            freq[i] += 1

        
        #Create heap with map keys as value ---> O(n)

        minheap = [val for val in freq.keys()]
        heapq.heapify(minheap)

        # while heap is True check for each group

        while minheap: 
            top = minheap[0]

            for i in range(top, top + groupSize): 
                if i not in freq:
                    return False

                freq[i] -= 1

                if freq[i] == 0:
                    if i != minheap[0]:
                        return False

                    heapq.heappop(minheap) #O(logn)

        return True

        
        # Time Complexity:
        # - Frequency map: O(n)
        # - Heapify: O(n)
        # - Processing cards with heap pops: O(n log n)
        # Overall: O(n log n)

        # Space Complexity:
        # - Frequency map + heap: O(n)

