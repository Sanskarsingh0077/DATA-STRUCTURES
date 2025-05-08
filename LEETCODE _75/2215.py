class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_a = set(nums1)
        set_b = set(nums2)
        
        res1 , res2 = set(),set()

        for n in set_a:
            if n not in set_b:
                res1.add(n)
        
        for n in set_b:
            if n not in set_a:
                res2.add(n)


        return [list(res1),list(res2)]

# Convert both lists to sets to eliminate duplicates and allow set operations
# Initialize two empty result sets for elements unique to each set

# Loop through set_a:
#   - If element not in set_b, add to result1

# Loop through set_b:
#   - If element not in set_a, add to result2

# Return both results as lists inside a list



#Better and cleaner Code

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_a = set(nums1)
        set_b = set(nums2)

            #Main Logic
        only_in_a = list(set_a - set_b)
        only_in_b = list(set_b - set_a)

        return [only_in_a,only_in_b]