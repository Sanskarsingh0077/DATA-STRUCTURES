class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i != "]":
                stack.append(i)

            
            else:
                string=""
                while stack and stack[-1] !="[":
                    string=stack.pop()+string

                stack.pop()

                num=""
                while stack and stack[-1].isdigit():
                    num= stack.pop()+num

                stack.append(string*int(num))

        return ''.join(stack)

        '''
        Approach:

        -Their is another appproach of making two stacks one for storing numbers and one for characters but that will be not space efficient.
        
    •	Initialize an empty stack to help with decoding the string
	•	Loop through each character in the input
	•	If it’s not a closing bracket ], push it onto the stack
	•	If it’s a closing bracket ]:
	•	Pop characters to build the substring until an opening bracket [ is found
	•	Pop the [
	•	Pop digits (could be more than one) to get the number of repetitions
	•	Multiply the substring by that number
	•	Push the resulting string back onto the stack
	•	Finally, join all elements in the stack to get the decoded result





        '''