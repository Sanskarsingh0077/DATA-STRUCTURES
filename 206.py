# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #Base Case
        if head is None or head.next is None:
            return head
        
        #recursive case
        last = self.reverseList(head.next) #future head that is last in current list

        head.next.next = head
        head.next = None

        return last


        '''
        Approach(Recursion Based):

        •	Base Case: If the linked list is empty (head is None) or has only one node (head.next is None), then it’s already reversed — return head.
	    •	Recursive Step: Recursively reverse the rest of the list starting from head.next, which gives you the reversed smaller list’s head (last).
	    •	Reversing Current Link: After recursion returns, point the next node’s .next back to the current node (head) — this reverses the link direction.
	    •	Break Old Link: Set head.next to None to prevent cycles and disconnect the old forward pointer.
	    •	Return New Head: Return the head of the reversed list (last) to the previous recursive call or to the caller.

        This method reverses the list using recursion, working its way to the end and flipping pointers as the stack unwinds.

        Approach(Stack Based):

        •	Step 1: Initialize a Stack :Create an empty stack to store all nodes of the linked list as you traverse.
	    •	Step 2: Push All Nodes to Stack :Start from the head, and push each node onto the stack until you reach the end (None).
	    •	Step 3: Pop the First Node (New Head): Pop the top node from the stack — this will become the new head of the reversed list.
	    •	Step 4: Re-link Nodes in Reverse Order: Continue popping nodes one by one. For each popped node, set the .next of the previous node to the current node.
	    •	Step 5: Terminate the List: After all nodes are re-linked, make sure to set the .next of the last node to None to mark the end of the list.
	    •	Step 6: Return New Head: Return the new head that was popped first from the stack.
        '''

        