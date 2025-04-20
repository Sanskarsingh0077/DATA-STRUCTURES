class Solution:
    def removeStars(self, s: str) -> str:
        stk=[]

        for i in s:
            if i == "*":
                stk.pop()
            else:
                stk.append(i)

        return ''.join(stk)


        '''
        Approach Explanation:
	1.	Use a Stack (List) to Simulate the String Processing:
	    •	Create an empty list stk to simulate a stack.
	    •	This will hold the characters of the string that are not yet removed.
	2.	Iterate Through Each Character in the Input String s:
	    •	For every character:
	    •	If the character is not '*', it means it’s a valid character that should be kept, so you append it to the  stack.
	    •	If the character is '*', it acts as a backspace/delete operator. So, you remove the last character added to the stack using pop() (i.e., delete the character just before this '*').
	3.	Build the Final Result:
	    •	After processing all characters, the stack contains only those characters that weren’t removed by a '*'.
	    •	Combine all the characters from the stack into a string using ''.join() and return the final result.

        	Time Complexity: O(n)
	    	Space Complexity: O(n)


        #Original code First wrote:

        stack = []

        for i in range(len(s)):
            stack.append(s[i])  # O(1)
            if s[i] == "*":  # O(1)
                if len(stack) >= 2:  # O(1)
                    stack.pop()  # O(1)
                        stack.pop()  # O(1)

        return ''.join(stack)  # O(n)

        '''