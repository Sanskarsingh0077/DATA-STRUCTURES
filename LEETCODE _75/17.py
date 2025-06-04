class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        def solve(idx: int, digits: str, temp: List[str], maps: Dict[str,str]):
            if idx>=len(digits):
                result.append("".join(temp))
                return
            
            ch = digits[idx]
            string = maps[ch]

            for i in range(len(string)):
                
                temp.append(string[i]) #do
                solve(idx+1,digits,temp,maps) #explore
                temp.pop() #undo 1

        #Solve Ends here
        
        map_array = {'2' : "abc", '3' : "def", '4' : "ghi", '5' : "jkl", '6' : "mno", '7' : "pqrs", '8' : "tuv", '9' : "wxyz"}

        if len(digits) == 0:
            return []
        
        temp = []

        solve(0,digits,temp,map_array)

        return result


    '''
    Approach(Backtracking):

    1.	Mapping:
	    •	A dictionary (map_array) maps digits ('2' to '9') to their respective letters, like '2': "abc".
	2.	Base Case:
	    •	If the input digits string is empty, return an empty list immediately — there’s nothing to process.
	3.	Backtracking Function (solve):
        •	Parameters:
        •	idx: current index in the digits string.
        •	digits: the original input string.
        •	temp: temporary list of characters building the current combination.
        •	maps: the digit-to-letters dictionary.
        •	Logic:
        •	If idx is beyond the last digit, the full combination is built → append to result.
        •	Otherwise, get the current digit, find the corresponding letters from maps.
        •	For each letter:
        •	Append it to temp (choose).
        •	Recurse to the next index (explore).
	    •	Remove the last letter after recursion (un-choose / backtrack).
	4.	Start the Backtracking:
	    •	Start from index 0 with an empty temp list.
	5.	Return the Result:
	    •	After the backtracking completes, return the result list containing all combinations.

    Time Complexity:
	•	Worst case: If there are n digits, and each maps to k letters (max 4 for '7' and '9'), the number of combinations is O(k^n).

    Space Complexity:
	•	O(n) auxiliary stack space for the recursion, and O(k^n) to store combinations.
    '''