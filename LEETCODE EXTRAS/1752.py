class Solution:
    def check(self, nums: List[int]) -> bool:
        count=0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1)%len(nums)]: #Circular Comparison
                count+=1
                if count>1:
                    return False
        
        return True
        
        '''
        Step-by-Step Approach:
            1.	Initialize a counter count = 0.
            2.	Loop through the array, comparing each element with the next element (nums[i] > nums[(i+1) % n]).
            •	Use modulo % to wrap around the last index to the first (circular check).
            3.	Every time you find such a “break”, increment count.
            4.	If count > 1, return False.
            5.	Otherwise, return True.

        Time: O(n) — single pass through the array
	•	Space: O(1) — constant space used


        '''
        