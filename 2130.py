# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #Approach 1: Convert nodes(values) to list and use two Pointer one from starting and one from end.
        list_1=[]
        
        while head is not None:
            list_1.append(head.val)
            head=head.next

        i=0
        j=len(list_1)-1
        max_sum= 0

        while i <len(list_1):
            curr_sum= list_1[i]+list_1[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
            i+=1
            j-=1

        return max_sum

    '''
        Convert to List + Two Pointers

    Idea:
	•	Traverse the entire linked list once to copy all node values into a Python list.
	•	Use two pointers:
	•	One starting from the beginning (i = 0)
	•	One from the end (j = len - 1)
	•	At each step, compute the sum list[i] + list[j] and track the maximum.
	•	Move i++, j-- until they meet or cross.

    Time Complexity:
	•	O(n) (one full traversal + another for two-pointer processing)

    Space Complexity:
	•	O(n) (for storing the node values in a list)


    #Approach 2: Using Stacks

    Idea:
	•	Traverse the entire linked list and push all nodes (or just their values) onto a stack.
	•	Traverse again from the head, and in each step:
	•	Pop the top value from the stack (which gives the twin of the current node)
	•	Add it to the current node’s value
	•	Track the maximum twin sum
	•	The stack provides reverse access without converting the entire list into a Python list.

    Time Complexity:
	•	O(n) (two traversals: one to push, one to compute)

    Space Complexity:
	•	O(n) (stack holds all nodes/values)


    Approach 3: Using linked list manipulation(reverse other half)

    Idea:
	•	Use the fast and slow pointer approach to find the middle of the linked list.
	•	Reverse the second half of the linked list in-place.
	•	Now you can traverse the first half and the reversed second half in tandem:
	•	At each step, compute first.val + second.val
	•	Track the max twin sum
	•	Optional: Reverse the second half again to restore the original list.

    Time Complexity:
	•	O(n) (one pass to find mid, one to reverse, one to compute sums)

    Space Complexity:
	•	O(1) (in-place reversal, no extra data structures used)

    '''  


        

        