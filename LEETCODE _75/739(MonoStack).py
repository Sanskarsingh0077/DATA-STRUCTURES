class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        
        #Brute Force O(n*n)
        '''
        ans = []
        

        for i in range(len(t)):
            found = False
            for j in range(i+1,len(t)):
                if t[i] < t[j]:
                    ans.append(j-i)
                    found = True
                    break

            if not found:
                ans.append(0)


        return ans

        # T C : O(n^2)
        '''

        # Monotonic Stack : Store indices in stack to keep track of positions.

        n = len(t)
        stack = []
        result = [0]*n
        
        for i in range(n-1,-1,-1):
            while stack and t[i] >= t[stack[-1]]: #The value in t at the index currently on top of the stack
                stack.pop()
            
            if not stack:
                result[i] = 0
            
            else:
                result[i] = stack[-1] - i

            stack.append(i)
                

        return result

        # T C : O(n) -  Each value checked only once

        '''
        Approach: Monotonic Stack (Right to Left) – Daily Temperatures
        1.	Goal: For each day, find how many days until a warmer temperature occurs. If no warmer day exists, store 0.
        2.	Use a stack to store indices of days with temperatures in decreasing order from right to left.
        3.	Traverse the list t from right to left:
            •	While the stack is not empty and the current temperature is greater than or equal to the temperature at the top index of the stack:
            •	Pop the stack (those days are not useful anymore).
            •	If the stack is not empty, the top of the stack is the next warmer day.
            •	Store the difference of indices in result[i].
            •	If the stack is empty, store 0 (no warmer day ahead).
            •	Push current index onto the stack.
	    4.	Return the result list.
        '''




