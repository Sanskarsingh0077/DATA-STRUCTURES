class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack=[]

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]: # If current asteroid is moving left and top of stack is moving right
                if abs(asteroid) > stack[-1]: # If the current asteroid is larger (in absolute value), pop the one on top of the stack
                    stack.pop()
                    continue  # Check again if more collisions happen
                elif abs(asteroid) == stack[-1]: # If they are of equal size, both destroy each other
                    stack.pop()
                    break # Both asteroids destroy each other, stop checking
                else:
                    break  # Current asteroid is destroyed, stop checking

            else:
                stack.append(asteroid) # If no collision happens, or the asteroid survives, push it to the stack

        return stack



        '''
         Approach (Using Stack):
	1.	Initialize an empty stack to simulate asteroid collisions.
	2.	Iterate over each asteroid:
	    •	If it’s positive (moving right), push it onto the stack.
	    •	If it’s negative (moving left), check for collisions:
	    •	While the top of the stack is positive and smaller than the current asteroid:
	    •	Pop the top (it explodes).
	    •	If top is equal in size (opposite sign), pop both (they destroy each other).
	    •	If top is larger, the current asteroid is destroyed (do not push it).
	3.	If no collision or it survives, push the current asteroid to the stack.
	4.	After all iterations, return the stack as the result.
        
        Time Complexity: O(n) — Each asteroid is pushed and popped at most once.

        Space Complexity: O(n) — Stack can hold all asteroids in the worst case (no collisions).

        '''
