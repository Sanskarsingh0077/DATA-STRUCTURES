def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        minElement = float('inf')
        map_values = {}

        # Count each element in basket1
        for x in basket1:
            if x not in map_values:
                map_values[x] = 0
            map_values[x] += 1
            minElement = min(minElement, x)

        # Subtract each element in basket2
        for x in basket2:
            if x not in map_values:
                map_values[x] = 0
            map_values[x] -= 1
            minElement = min(minElement, x)

        finalList = []

        # Check for imbalance and collect elements to be swapped
        for cost , count in map_values.items():
            if count == 0:
                continue
            
            if count % 2 != 0:
                return -1

            for i in range(1,(abs(count)//2)+1):
                finalList.append(cost)

        finalList.sort() # Sort to minimize swap cost

        result = 0
        half = len(finalList)//2 # We only need to do half the swaps

        # Calculate minimal cost using direct swap or through minElement as intermediary
        for i in range(half):
            result += min(finalList[i], 2*minElement)

        return result



        
        # Algorithm
        '''

        	•	Balances the difference between the two baskets.
            •	If a value is present more times in one basket than the other, that surplus must be corrected via swapping.
            •	The total number of values to be swapped is always even; otherwise, it’s impossible (return -1).
            •	Swaps are performed using the cheaper of:
            •	direct swap of mismatched elements
            •	or a double-swap through the smallest element (which can be cheaper).

            Total Time Complexity: O(n + k log k)
            where:
            •	n is the total number of items in both baskets
            •	k is the number of elements to swap (can be up to n in worst case)

            Total Space Complexity: O(n)

        '''