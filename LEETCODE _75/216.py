class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def solve(curr,k,n,start):
            if k == 0 and n == 0:
                result.append(curr)
                return
            
            if k <= 0:
                return
            
            for i in range(start,min(10,n+1)):
                solve(curr+[i],k-1,n-i, i+1)
            return
        
        if k > n:
            return []

        solve([],k,n,1)

        return result

        '''
         Approach (Backtracking):
            1.	Use recursion and backtracking to explore all possible combinations of numbers 1 to 9.
            2.	Maintain:
                •	curr: the current combination being formed.
                •	k: how many numbers still need to be picked.
                •	n: remaining target sum.
                •	start: the starting number to ensure no repetition and maintain increasing order.
            3.	Base Conditions:
                •	If k == 0 and n == 0: a valid combination is formed → add to result.
                •	If k <= 0 or n < 0: invalid path → stop exploring.
            4.	Recursive Step:
                •	Loop from start to 9 (only once per number).
                •	At each step:
                •	Add the number to the current combination.
                •	Recurse with updated k, n, and start + 1.
                •	Backtrack by removing the last added number.

            •	Time complexity: O( C(9, k) ), where C(9, k) is the number of k-combinations of numbers 1–9.
	        •	Space complexity: O(k) for recursion stack + O(#valid_combinations) for result.
        '''
        