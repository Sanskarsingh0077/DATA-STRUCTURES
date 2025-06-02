class Solution:
    import math
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        #Best Solution Using Binary Search and not using any python module like bisect to get index

        #Function to search minPotion index
        def get_index_of(start,end,sorted_array,elementToSearch):
    
            while start <= end:
                mid = start + (end-start)//2
                if sorted_array[mid] >= elementToSearch:
                    possible_index = mid
                    end = mid-1
                else:
                    start = mid+1

            return possible_index
                
        #function ends here
        potions.sort()
        pairs = []
        n = len(potions)
        m = len(spells)
        maxPotionValue = potions[n-1]

        for i in range(m):
            spell = spells[i]
            minPotion = math.ceil((1.0*success)/spell) # spell * potions[j] >= success ⇒ potions[j] >= success / spell

            if minPotion > maxPotionValue:
                pairs.append(0)
                continue

            index = get_index_of(0,n-1,potions,minPotion)#gets the lowest point index in potion

            count = n-index 

            pairs.append(count)

        return pairs





        #Brute Force but Passing 51/57 cases goes till 10^4 Gives TLE
        '''
        pairs = []
        count=0

        for i in range(len(spells)):
            for j in range(len(potions)):
                if spells[i]*potions[j]>=success:
                    count +=1
            
            pairs.append(count)
            count = 0
        
        return pairs
        '''
        '''
        #Using Binary Search with using bisect module to get index of minPotion

        potions.sort()
        pairs = []

        n = len(potions)
        m = len(spells)
        maxPotionValue = potions[n-1]

        for i in range(m):
            spell = spells[i]
            minPotion = math.ceil((1.0*success)/spell) # spell * potions[j] >= success ⇒ potions[j] >= success / spell

            if minPotion > maxPotionValue:
                pairs.append(0)
                continue

            index = bisect.bisect_left(potions, minPotion) #gets the lowest point index in potion

            count = n-index 

            pairs.append(count)

        return pairs
        '''

        '''
        Approach:

        	1.	Sort the potions list to allow binary search.
            2.	For each spell in spells:
                •	Calculate the minimum potion value needed: minPotion = ceil(success / spell)
                •	If minPotion is greater than the maximum potion value, append 0 (no successful pairs).
                •	Otherwise, use binary search (bisect_left) to find the first potion ≥ minPotion.
                •	Count how many potions from that index to the end → these are successful.
            3.	Append the count for each spell to the result list.
            4.	Return the result list.

            Time Complexity:
	        1.	Sorting potions: O(n log n)
	        2.	Processing each spell (binary search on potions): For each of the m spells, you perform a bisect_left (binary search), which takes O(log n) time.
            ⇒ Total for all spells: O(m log n)

            Space Complexity:
            •	O(1) extra space if we don’t count the result list.
            •	O(m) for the result list storing counts per spell.
            Total Space Complexity: O(m) (output list only; rest is in-place)
        '''





        
        