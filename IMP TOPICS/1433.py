class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1=''.join(sorted(s1))
        s2 = ''.join(sorted(s2))

        s1_break_s2 = True
        s2_break_s1 = True

        for i in range(len(s1)):
            if s1[i]< s2[i]:
                s1_break_s2 = False
            if s1[i]> s2[i]:
                s2_break_s1 = False
            
        
        return s2_break_s1 or s1_break_s2
        
'''
Approach (Sorted Comparison):
	1.	Sort both strings:
        •	Sorting aligns the characters of both strings in increasing order.
        •	This allows direct index-wise comparison to check the “can break” condition.
	2.	Use flags to track dominance:
        •	Use two boolean flags:
        •	s1_break_s2: becomes False if s1[i] < s2[i] at any index.
        •	s2_break_s1: becomes False if s2[i] < s1[i] at any index.
        •	This checks if one full string dominates the other across all positions.
	3.	Return result:
	    •	If either flag remains True after the loop, it means one string can break the other.

    •	Time: O(n log n) for sorting each string.
	•	Space: O(n) due to the sorted copies of the strings.

'''
