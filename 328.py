# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head


        odd= head
        even = head.next

        evenStart = head.next

        while even is not None and even.next is not None:


            odd.next = even.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        
        odd.next = evenStart

        return head


        '''
        Approach:

        •	Step 1: Check if the list has 0 or 1 nodes — if yes, return head directly (no rearrangement needed).
        •	Step 2: Initialize two pointers:
        odd starting at the first node (head) and even at the second node (head.next).
        •	Step 3: Save the start of even list (evenStart) to connect it later.
        •	Step 4:
        Traverse the list:
            •	Connect odd.next to the node after even.
            •	Connect even.next to the node after the new odd.
            •	Move both odd and even pointers one step forward.
        •	Step 5: After loop, attach the even list (evenStart) at the end of the odd list.
        •	Step 6: Return the modified head.
        
        Complexities:

        : Time Complexity: O(n) - traversing the linked list exactly once. Each node is visited only one time — either by the odd or the even pointer.
        : Space Complexity: O(1) - using only a fixed number of pointers (odd, even, evenStart). No extra data structures (like arrays, lists) proportional to the input size.



        '''


        
