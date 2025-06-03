class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #function to check if bananas eaten and in how many hours
        def canEatAllbananas(pile_array,min_value,hours):
            actualhours = 0
            for i in range(len(pile_array)):
                actualhours += pile_array[i]//min_value #get hours 
                if pile_array[i]%min_value != 0: #get remaining bananas hours
                    actualhours+=1
            
            return actualhours <= hours #return True or False


        n = len(piles)
        
        lowest = 1
        highest = max(piles)

        #Basic Binary Search in 1 to max bananas list
        while lowest < highest:
            min_value = lowest + (highest-lowest)//2 


            if canEatAllbananas(piles,min_value,h):
                highest = min_value
            else:
                lowest = min_value + 1

        return lowest

        '''
        Approach:

        	1.	Define Search Space:
                •	The minimum possible eating speed is 1.
                •	The maximum possible speed is max(piles) (if Koko eats a whole pile per hour).
	        2.	Binary Search:
	            •	Use binary search in the range [1, max(piles)] to find the minimum valid speed k.
	        3.	Check Feasibility:
	            •	For each candidate speed (min_value), define a helper function canEatAllbananas() to calculate if Koko can eat all bananas within h hours.
	            •	For each pile:
	            •	Time to eat it = pile // k
	            •	If not perfectly divisible, she needs one extra hour for the remainder.
	            •	Or better yet: ceil(pile / k)
	        4.	Narrow the Search:
	            •	If the current speed is sufficient (canEatAllbananas() is True), try to find a smaller valid speed → move highest = mid
	            •	Else, speed is too slow → move lowest = mid + 1
	        5.	Return the Result:
	            •	The first speed that passes the check is your answer.

            Time and Space Complexity:
	        •	Time Complexity: O(n * log m) where:
            •	n = number of piles
            •	m = max number of bananas in any pile (range of search)
	        •	Space Complexity: O(1) — no extra space used beyond variables.
        '''






